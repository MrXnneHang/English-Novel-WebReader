<template>
  <div>
    <!-- 头部组件 -->
    <Header :onFileChange="onFileChange" />

    <!-- 包含左右文本页的容器组件 -->
    <Container
        :pages="pages"
        :currentPageIndex="currentPageIndex"
        :handleScroll="handleScroll"
        :handleTextSelection="handleTextSelection"
        :text-selected="showMessageBubble"
    />

    <!-- 页脚组件，包含翻页功能 -->
    <Footer
        :prevPage="prevPage"
        :nextPage="nextPage"
        :goToPage="goToPage"
        :totalPages="totalPages"
        :readingProgress="readingProgress"
    />

    <!-- 消息气泡组件 -->
    <MessageBubble v-if="showBubble" :text="selectedText" />
  </div>
</template>

<script>
import Header from './components/EbookHeader.vue';
import Container from './components/TextContainer.vue';
import Footer from './components/EbookFooter.vue';
import MessageBubble from './components/MessageBubble.vue';  // 引入消息气泡组件

export default {
  components: {
    Header,
    Container,
    Footer,
    MessageBubble  // 注册消息气泡组件
  },
  data() {
    return {
      fileContent: '',
      pages: [],
      currentPageIndex: 0,
      recordedWords: [],
      showBubble: false,  // 控制消息气泡显示
      selectedText: '',    // 存储选中的文本
    };
  },
  computed: {
    totalPages() {
      return this.pages.length;
    },
    readingProgress() {
      if (this.totalPages === 0) return 0;
      return Math.floor(((this.currentPageIndex + 2) / this.totalPages) * 100);
    },
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.fileContent = e.target.result;
          this.paginateText();
        };
        reader.readAsText(file);
      }
    },
    paginateText() {
      this.pages = [];
      const linesPerPage = 30;
      const maxLineLength = 90;
      const indentSize = 3;
      const indent = ' '.repeat(indentSize);
      const lines = this.fileContent.split('\n');
      let currentPage = '';
      let currentLineCount = 0;
      let tempLine = '';
      let isParagraphStart = true;

      lines.forEach((line) => {
        const words = line.split(' ');
        words.forEach((word) => {
          if ((tempLine + word).length > maxLineLength) {
            if (isParagraphStart) {
              currentPage += indent + tempLine.trim() + '\n';
              isParagraphStart = false;
            } else {
              currentPage += tempLine.trim() + '\n';
            }

            currentLineCount += 1;
            if (currentLineCount >= linesPerPage) {
              this.pages.push(currentPage);
              currentPage = '';
              currentLineCount = 0;
            }
            tempLine = '';
          }
          tempLine += word + ' ';
        });

        if (tempLine.trim() !== '') {
          if (isParagraphStart) {
            currentPage += indent + tempLine.trim() + '\n';
            isParagraphStart = false;
          } else {
            currentPage += tempLine.trim() + '\n';
          }

          tempLine = '';
          currentLineCount += 1;
          if (currentLineCount >= linesPerPage) {
            this.pages.push(currentPage);
            currentPage = '';
            currentLineCount = 0;
          }
        } else {
          isParagraphStart = true;
        }
      });

      if (currentPage.trim() !== '') {
        this.pages.push(currentPage);
      }
    },
    handleScroll(event) {
      if (event.deltaY > 0) {
        this.nextPage();
      } else if (event.deltaY < 0) {
        this.prevPage();
      }
    },
    prevPage() {
      if (this.currentPageIndex > 1) {
        this.currentPageIndex -= 2;
      }
    },
    nextPage() {
      if (this.currentPageIndex + 2 < this.pages.length) {
        this.currentPageIndex += 2;
      }
    },
    goToPage(pageNumber) {
      const targetIndex = (pageNumber - 1) * 2;
      if (targetIndex >= 0 && targetIndex < this.pages.length) {
        this.currentPageIndex = targetIndex;
      }
    },
    async handleTextSelection(selectedText) {
      if (selectedText) {
        console.log("Selected text: ", selectedText);
        this.recordedWords.push(selectedText);

        try {
          const response = await fetch('http://localhost:5000/api/selected-word', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({selectedText}),
          });

          const data = await response.json();
          console.log('Response from server:', data);

          // 在请求成功后，显示消息气泡
          this.showMessageBubble(selectedText);
        } catch (error) {
          console.error('Error sending selected word:', error);

          // 在请求失败时，显示错误的消息气泡
          this.showMessageBubble('Error sending text to server.');
        }
      }
    },
    // 消息气泡显示逻辑
    showMessageBubble(message) {
      console.log('Showing message bubble with text:', message); // Debug line
      this.selectedText = message;
      this.showBubble = true;
    }
  },
};
</script>
