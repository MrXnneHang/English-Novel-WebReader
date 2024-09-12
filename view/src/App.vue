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
    />

    <!-- 页脚组件，包含翻页功能 -->
    <Footer
        :prevPage="prevPage"
        :nextPage="nextPage"
        :goToPage="goToPage"
        :totalPages="totalPages"
        :readingProgress="readingProgress"
    />
  </div>
</template>

<script>
import Header from './components/EbookHeader.vue';
import Container from './components/TextContainer.vue';
import Footer from './components/EbookFooter.vue';

export default {
  components: {
    Header,
    Container,
    Footer,
  },
  data() {
    return {
      fileContent: '', // 存储整个文件内容
      pages: [], // 分页后的文本
      currentPageIndex: 0, // 当前页码索引
      recordedWords: [], // 新增：记录已选择的单词
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
      const indentSize = 3;  // 设定段落首行缩进字符数
      const indent = ' '.repeat(indentSize); // 根据缩进大小生成空格字符串
      const lines = this.fileContent.split('\n');
      let currentPage = '';
      let currentLineCount = 0;
      let tempLine = '';
      let isParagraphStart = true;  // 标记是否是段落的首行

      lines.forEach((line) => {
        const words = line.split(' ');
        words.forEach((word) => {
          if ((tempLine + word).length > maxLineLength) {
            // 添加段落首行缩进
            if (isParagraphStart) {
              currentPage += indent + tempLine.trim() + '\n';
              isParagraphStart = false;  // 标记该段落已开始
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

        // 判断换行是否是段落结束（即空行）
        if (tempLine.trim() !== '') {
          // 添加段落首行缩进
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
          // 空行表示段落结束，下一行是新段落的开始
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

        // 将选中的单词发送到后端，修改为后端的端口 5000
        try {
          const response = await fetch('http://localhost:5000/api/selected-word', { // 使用后端端口 5000
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ selectedText }),
          });

          // 解析 JSON 响应
          const data = await response.json();
          console.log('Response from server:', data);
        } catch (error) {
          console.error('Error sending selected word:', error);
        }
      }
    }
  },
};
</script>
