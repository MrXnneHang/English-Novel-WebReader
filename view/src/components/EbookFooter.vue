<template>
  <div class="footer">
    <button @click="prevPage">Previous Page</button>

    <!-- 输入框用于跳转到特定页码 -->
    <input type="number" v-model="targetPage" @keydown.enter="triggerGoToPage" min="1" :max="totalPages" />

    <button @click="nextPage">Next Page</button>
    <p>Total Pages: {{ totalPages }}</p>
  </div>
</template>

<script>
export default {
  props: {
    prevPage: Function,    // 上一页方法
    nextPage: Function,    // 下一页方法
    goToPage: Function,    // 父组件传递的跳转方法
    totalPages: Number,    // 总页数
  },
  data() {
    return {
      targetPage: 1, // 用户输入的目标页码
    };
  },
  methods: {
    // 本地方法，调用传递的 goToPage 方法
    triggerGoToPage() {
      // 检查输入的页码是否在范围内
      if (this.targetPage >= 1 && this.targetPage <= this.totalPages) {
        this.goToPage(this.targetPage); // 调用传递的 goToPage
      }
    },
  },
};
</script>

<style scoped>
.footer {
  padding: 20px;
  text-align: center;
}
button {
  margin: 0 10px;
  padding: 10px;
  font-size: 16px;
}
input {
  width: 50px;
  margin: 0 10px;
  padding: 10px;
  text-align: center;
}
p {
  display: inline;
  font-size: 16px;
}
</style>
