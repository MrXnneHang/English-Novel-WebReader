<template>
  <div>
    <!-- 头部组件 -->
    <Header :title="bookTitle" :onFileChange="onFileChange" />

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
import Header from '@/components/EbookHeader.vue';
import Container from '@/components/TextContainer.vue';
import Footer from '@/components/EbookFooter.vue';
import MessageBubble from '@/components/MessageBubble.vue';

export default {
  name: 'EbookReader',
  components: {
    Header,
    Container,
    Footer,
    MessageBubble
  },
  data() {
    return {
      fileContent: '',  // 文件内容
      pages: [],
      currentPageIndex: 0,
      recordedWords: [],
      showBubble: false,
      selectedText: '',
      bookTitle: this.$route.params.bookTitle // 从路由参数中获取书名
    };
  },
  created() {
    const bookPath = this.$route.params.bookPath;
    if (bookPath) {
      this.loadBookFromPath(bookPath);
    }
  },
  methods: {
    // 加载书籍内容
    async loadBookFromPath(bookPath) {
      try {
        const response = await fetch(`http://localhost:5000/api/load_book_content`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({bookPath})
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        this.fileContent = data.fileContent;  // 假设后端返回书籍的文本内容
        this.paginateText();  // 分页显示
      } catch (error) {
        console.error('Error loading book from path:', error);
      }
    },
    paginateText() {
      const newPages = [];
      const linesPerPage = 22;
      const maxLineLength = 75;
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
              newPages.push(currentPage);
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
            newPages.push(currentPage);
            currentPage = '';
            currentLineCount = 0;
          }
        } else {
          isParagraphStart = true;
        }
      });

      if (currentPage.trim() !== '') {
        newPages.push(currentPage);
      }

      this.pages = newPages;
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

        this.showMessageBubble('Waiting for message...');

        try {
          const response = await fetch('http://localhost:5000/api/selected-word', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({selectedText}),
          });

          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          const data = await response.json();
          this.updateMessageBubble(data.message);
        } catch (error) {
          console.error('Error sending selected word:', error);
          this.updateMessageBubble('Error sending text to server.');
        }
      }
    },

    showMessageBubble(message) {
      console.log('Showing message bubble with text:', message);
      this.selectedText = message;
      this.showBubble = true;

      if (this.autoCloseTimer) {
        clearTimeout(this.autoCloseTimer);
      }
    },

    updateMessageBubble(newMessage) {
      this.selectedText = newMessage;

      if (this.autoCloseTimer) {
        clearTimeout(this.autoCloseTimer);
      }

      this.autoCloseTimer = setTimeout(() => {
        this.showBubble = false;
      }, 10000); // 10秒后隐藏消息气泡
    },
  },
  computed: {
    totalPages() {
      return this.pages.length;
    },
    readingProgress() {
      if (this.totalPages === 0) return 0;
      return Math.floor(((this.currentPageIndex + 2) / this.totalPages) * 100);
    }
  }
};
</script>
