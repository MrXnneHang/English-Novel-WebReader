import Vue from 'vue';
import Router from 'vue-router';
import Bookshelf from '@/views/BookShelf.vue';
import EbookReader from '@/views/EbookReader.vue';

// 使用 Router
Vue.use(Router);

export default new Router({
  mode: 'history',  // 使用 HTML5 的历史模式
  routes: [
    {
      path: '/',
      name: 'Bookshelf',
      component: Bookshelf,
    },
    {
      path: '/reader/:bookId',
      name: 'EbookReader',
      component: EbookReader,
    },
  ],
});
