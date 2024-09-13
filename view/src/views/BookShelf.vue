<template>
  <div>
    <!-- Header Component -->
    <BookshelfHeader />

    <!-- Body Component -->
    <BookshelfBody :books="books" @openBook="openBook" />
  </div>
</template>

<script>
import BookshelfHeader from '@/components/BookshelfHeader.vue';
import BookshelfBody from '@/components/BookshelfBody.vue';
import axios from 'axios';

export default {
  name: 'BookShelf',
  components: {
    BookshelfHeader,
    BookshelfBody,
  },
  data() {
    return {
      books: [], // 初始化空的书籍列表
    };
  },
  created() {
    this.fetchBooks(); // 当组件创建时获取书本列表
  },
  methods: {
    // 获取书籍列表
    async fetchBooks() {
      try {
        const response = await axios.get('http://localhost:5000/api/get_book_list');
        console.log("Fetched books:", response.data); // 调试输出API数据
        this.books = response.data; // 将书籍数据赋值给 books
      } catch (error) {
        console.error("Failed to fetch books:", error);
        alert('Error fetching books, please try again later.');
      }
    },
    // 打开电子书阅读器页面
    async openBook(book) {
      try {
        // 获取书籍绝对路径
        const response = await axios.post('http://localhost:5000/api/get_book_abs_path', { book_title: book.title });
        const bookAbsPath = response.data.book_abs_path;
        console.log('Book absolute path:', bookAbsPath);

        // 跳转到 EbookReader 页面并传递路径
        this.$router.push({ name: 'EbookReader', params: { bookPath: bookAbsPath } });
      } catch (error) {
        console.error('Failed to fetch book path:', error);
      }
    }

  },
};
</script>

<style scoped>
/* 为整个书架组件添加样式 */
</style>
