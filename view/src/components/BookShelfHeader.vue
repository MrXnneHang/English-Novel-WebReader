<template>
  <header class="header">
    <h1>Bookshelf</h1>
    <div class="button-container">
      <button @click="importBooks" class="import-button">Import Books</button>
      <p class="format-hint">Supports: txt, epub</p>
    </div>
  </header>
</template>

<script>
export default {
  name: 'BookshelfHeader',
  methods: {
    importBooks() {
      // 处理导入书籍的逻辑，比如打开文件选择器
      alert('Import Books button clicked!');
    },
  },
};
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #f5f5f5;
}

h1 {
  margin: 0;
}

.button-container {
  margin-left: auto; /* 使按钮靠右对齐 */
  text-align: right;
}

.import-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  cursor: pointer;
}

.import-button:hover {
  background-color: #45a049;
}

.format-hint {
  margin-top: 5px;
  font-size: 12px;
  color: gray;
}
</style>
