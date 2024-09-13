<template>
  <div class="bookshelf-container">
    <div class="bookshelf">
      <!-- 删除调试输出，保持页面简洁 -->
      <div v-for="(book, index) in formattedBooks" :key="index" class="book">
        <p v-if="book.id !== null">{{ book.title }}</p>
        <button v-if="book.id !== null" @click="openBook(book)">Open</button>
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
    // 确保总共12个位置，如果书不够则用空位置补足
    formattedBooks() {
      const totalSlots = 12; // 2行x6列，总共12个位置
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
  grid-template-columns: repeat(6, 100px); /* 6 列，每列 100px */
  grid-template-rows: repeat(2, 200px); /* 2 行，每行 200px */
  justify-content: center; /* 水平居中 */
  gap: 200px; /* 书籍之间的间距 */
}

.book {
  width: 250px;
  height: 350px;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
  box-sizing: border-box;
}

.book p {
  margin: 0;
  font-size: 16px;
}

.book button {
  margin-top: auto; /* 按钮固定在底部 */
}

.book:empty {
  visibility: hidden; /* 隐藏空书籍项，保持布局 */
}
</style>
