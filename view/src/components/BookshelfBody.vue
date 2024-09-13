<template>
  <div class="bookshelf-container">
    <div class="bookshelf">
      <div v-for="(book, index) in formattedBooks" :key="index" class="book" @click="openBook(book)">
        <p v-if="book.id !== null">{{ book.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookshelfBody',
  props: {
    books: {
      type: Array,
      required: true,
    },
  },
  computed: {
    // 确保总共10个位置，如果书不够则用空位置补足
    formattedBooks() {
      const totalSlots = 10;
      const filledBooks = [...this.books];
      while (filledBooks.length < totalSlots) {
        filledBooks.push({id: null, title: ''});
      }
      return filledBooks;
    },
  },
  methods: {
    openBook(book) {
      if (book.id !== null) {
        this.$emit('openBook', book); // 触发父组件的openBook事件
      }
    },
  },
};
</script>

<style scoped>
.bookshelf-container {
  padding-top: 50px; /* 与 Header 之间的 100px 间距 */
  padding-bottom: 50px; /* 与底部之间的 100px 间距 */
}

.bookshelf {
  display: grid;
  grid-template-columns: repeat(5, 300px); /* 5 列，每列 300px */
  grid-template-rows: repeat(2, 400px); /* 2 行，每行 400px */
  justify-content: center; /* 水平居中 */
  gap: 20px; /* 书籍之间的间距 */
}

.book {
  width: 300px;
  height: 400px;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  box-sizing: border-box;
  cursor: pointer; /* 添加鼠标悬停效果，提示可点击 */
  transition: transform 0.3s ease; /* 添加缩放过渡效果 */
}

.book:hover {
  transform: scale(1.05); /* 鼠标悬停时缩放效果 */
}

.book p {
  margin: 0;
  font-size: 20px; /* 调整字体大小 */
  font-weight: bold; /* 字体加粗 */
  color: #333; /* 字体颜色 */
}
</style>
