<template>
  <div class="container" @wheel="handleScroll" @mouseup="selectText">
    <!-- 左边部分，显示当前的左边页内容 -->
    <div class="left">
      <pre>{{ currentLeftPage }}</pre>
      <div class="page-number">Page {{ currentPageIndex + 1 }}</div>
    </div>

    <!-- 右边部分，显示当前的右边页内容 -->
    <div class="right">
      <pre>{{ currentRightPage }}</pre>
      <div class="page-number" v-if="currentPageIndex + 2 <= pages.length">Page {{ currentPageIndex + 2 }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    pages: Array,
    currentPageIndex: Number,
    handleScroll: Function,
    handleTextSelection: Function, // 接收处理文本选择的回调函数
  },
  computed: {
    currentLeftPage() {
      return this.pages[this.currentPageIndex] || '';
    },
    currentRightPage() {
      return this.pages[this.currentPageIndex + 1] || '';
    },
  },
  methods: {
    selectText() {
      console.log("Mouse up event triggered"); // 调试日志
      const selectedText = window.getSelection().toString().trim();
      if (selectedText) {
        console.log("Selected text: ", selectedText); // 调试日志
        this.handleTextSelection(selectedText); // 传递选中的文本
      } else {
        console.log("No text selected");
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  height: 80vh;
  overflow: hidden;
}

.left, .right {
  flex: 1;
  font-size: 24px;
  padding: 20px;
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow: hidden;
}

.left {
  background-color: #f0f0f0;
}

.right {
  background-color: #d0eaff;
}

.page-number {
  text-align: center;
  font-weight: bold;
  margin-top: 10px;
}
</style>
