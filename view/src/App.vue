<template>
  <div>
    <!-- 头部组件 -->
    <Header :onFileChange="onFileChange" />

    <!-- 包含左右文本页的容器组件 -->
    <Container
        :pages="pages"
        :currentPageIndex="currentPageIndex"
        :handleScroll="handleScroll"
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
      fileContent: '',     // 存储整个文件内容
      pages: [],           // 分页后的文本
      currentPageIndex: 0, // 当前页码索引
    };
  },
  computed: {
    totalPages() {
      // 返回分页的总数
      return this.pages.length;
    },
    readingProgress() {
      // 计算阅读进度百分比
      if (this.totalPages === 0) return 0;
      return Math.floor(((this.currentPageIndex + 2) / this.totalPages) * 100); // 计算百分比，处理双页显示
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
      const linesPerPage = 25;  // 每页最大行数
      const maxLineLength = 75; // 每行最大字符数
      const lines = this.fileContent.split('\n');
      let currentPage = '';
      let currentLineCount = 0;
      let tempLine = '';
      lines.forEach(line => {
        const words = line.split(' ');
        words.forEach(word => {
          if ((tempLine + word).length > maxLineLength) {
            currentPage += tempLine.trim() + '\n';
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
          currentPage += tempLine.trim() + '\n';
          tempLine = '';
          currentLineCount += 1;
          if (currentLineCount >= linesPerPage) {
            this.pages.push(currentPage);
            currentPage = '';
            currentLineCount = 0;
          }
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
  },
};
</script>
