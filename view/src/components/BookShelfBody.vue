<template>
  <div class="bookshelf">
    <div v-for="book in books" :key="book.id" class="book">
      <p>{{ book.title }}</p>
      <button @click="openBook(book)">Open</button>
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
  methods: {
    openBook(book) {
      this.$emit('openBook', book); // 将事件传递给父组件
    },
  },
};
</script>

<style scoped>
.bookshelf {
  display: flex;
  flex-wrap: wrap;
}

.book {
  margin: 10px;
  padding: 10px;
  border: 1px solid black;
  width: 150px;
  text-align: center;
}
</style>
