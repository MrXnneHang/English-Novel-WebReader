<template>
  <div>
    <!-- Header Component -->
    <BookshelfHeader />

    <!-- Body Component -->
    <BookshelfBody :books="books" @openBook="openBook" />
  </div>
</template>

<script>
import BookshelfHeader from '@/components/BookShelfHeader.vue';
import BookshelfBody from '@/components/BookShelfBody.vue';

export default {
  name: 'BookShelf',
  components: {
    BookshelfHeader,
    BookshelfBody,
  },
  data() {
    return {
      books: [
        {id: 1, title: 'Book 1'},
        {id: 2, title: 'Book 2'},
      ],
    };
  },
  methods: {
    openBook(book) {
      this.$router.push({name: 'EbookReader', params: {bookId: book.id}});
    },
  },
};
</script>
