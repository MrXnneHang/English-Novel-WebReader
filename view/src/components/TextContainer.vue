<template>
  <div class="container" @wheel="handleScroll">
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
    pages: Array,           // 接收分页数据
    currentPageIndex: Number, // 接收当前页码索引
    handleScroll: Function,   // 接收滚动事件处理
  },
  computed: {
    currentLeftPage() {
      return this.pages[this.currentPageIndex] || '';
    },
    currentRightPage() {
      return this.pages[this.currentPageIndex + 1] || '';
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
