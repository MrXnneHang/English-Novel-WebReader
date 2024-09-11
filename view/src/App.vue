<template>
  <div>
    <!-- 文件上传按钮 -->
    <div class="file-upload">
      <input type="file" @change="onFileChange" accept=".txt" />
    </div>

    <!-- 包含左右栏的容器 -->
    <div class="container" @wheel="handleScroll">
      <!-- 左边部分，显示当前的左边页内容 -->
      <div class="left">
        <pre>{{ currentLeftPage }}</pre>
      </div>

      <!-- 右边部分，显示当前的右边页内容 -->
      <div class="right">
        <pre>{{ currentRightPage }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fileContent: '',     // 存储整个文件内容
      pages: [],           // 分页后的文本
      currentPageIndex: 0, // 当前页码索引
    };
  },
  computed: {
    // 当前左侧页面的内容
    currentLeftPage() {
      return this.pages[this.currentPageIndex] || '';
    },
    // 当前右侧页面的内容
    currentRightPage() {
      return this.pages[this.currentPageIndex + 1] || '';
    },
  },
  methods: {
    // 当文件改变时触发
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

      // 临时存储单词的行
      let tempLine = '';

      lines.forEach(line => {
        // 将每行文本按空格分割成单词
        const words = line.split(' ');

        words.forEach(word => {
          // 如果当前行加上新单词超过最大字符数，先将当前行添加到当前页面
          if ((tempLine + word).length > maxLineLength) {
            currentPage += tempLine.trim() + '\n';
            currentLineCount += 1;

            // 如果当前页面行数达到最大值，推送当前页面并重置
            if (currentLineCount >= linesPerPage) {
              this.pages.push(currentPage);
              currentPage = '';
              currentLineCount = 0;
            }

            // 清空临时行
            tempLine = '';
          }

          // 将当前单词添加到临时行
          tempLine += word + ' ';
        });

        // 在处理完每行后，添加临时行到当前页面
        if (tempLine.trim() !== '') {
          currentPage += tempLine.trim() + '\n';
          tempLine = ''; // 清空临时行
          currentLineCount += 1;

          // 如果当前页面行数达到最大值，推送当前页面并重置
          if (currentLineCount >= linesPerPage) {
            this.pages.push(currentPage);
            currentPage = '';
            currentLineCount = 0;
          }
        }
      });

      // 添加最后剩余的内容作为一页
      if (currentPage.trim() !== '') {
        this.pages.push(currentPage);
      }
    },
    // 处理滚轮滚动事件，向下翻到下一组页面，向上翻到上一组页面
    handleScroll(event) {
      if (event.deltaY > 0) {
        // 向下滚动，翻到下一组页面
        this.nextPage();
      } else if (event.deltaY < 0) {
        // 向上滚动，翻到上一组页面
        this.prevPage();
      }
    },
    // 翻到上一组页面
    prevPage() {
      if (this.currentPageIndex > 1) {
        this.currentPageIndex -= 2; // 左右两页为一组，索引减2
      }
    },
    // 翻到下一组页面
    nextPage() {
      if (this.currentPageIndex + 2 < this.pages.length) {
        this.currentPageIndex += 2; // 左右两页为一组，索引加2
      }
    },
  },
};
</script>

<style scoped>

/* 文件上传按钮样式 */
.file-upload {
  padding: 20px;
  background-color: #f8f8f8;
  text-align: center;
}

/* input 样式，放大尺寸让用户更容易点击 */
input[type="file"] {
  padding: 10px;
  font-size: 16px;
}

/* 包含左右栏的容器样式 */
.container {
  display: flex; /* 使用 flexbox 布局 */
  height: 80vh; /* 占满屏幕剩余部分高度 */
  overflow: hidden; /* 隐藏超出容器的内容 */
}

/* 左侧样式 */
.left {
  flex: 1; /* 占据 50% 宽度 */
  background-color: #f0f0f0; /* 浅灰背景 */
  font-size: 24px; /* 字体大小 */
  padding: 20px;
  white-space: pre-wrap; /* 保留换行符并自动换行 */
  word-wrap: break-word; /* 确保长单词在容器宽度处换行 */
  overflow: hidden; /* 防止文本溢出 */
}

/* 右侧样式 */
.right {
  flex: 1; /* 占据 50% 宽度 */
  background-color: #d0eaff; /* 浅蓝背景 */
  font-size: 24px; /* 字体大小 */
  padding: 20px;
  white-space: pre-wrap; /* 保留换行符并自动换行 */
  word-wrap: break-word; /* 确保长单词在容器宽度处换行 */
  overflow: hidden; /* 防止文本溢出 */
}
</style>
