<template>
  <div class="book-title">
    <h1>{{ title }}</h1> <!-- 渲染书籍标题 -->
  </div>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      required: true, // 父组件传入的书籍标题
    },
  },
};
</script>

<style scoped>
.book-title {
  padding: 20px;
  background-color: #f8f8f8;
  text-align: center;
}

h1 {
  font-size: 24px;
  font-weight: bold;
}
</style>
