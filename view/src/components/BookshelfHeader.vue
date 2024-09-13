<template>
  <header class="header">
    <h1>Bookshelf</h1>
    <div class="button-container">
      <!-- 点击按钮触发文件选择 -->
      <button @click="importBooks" class="import-button">Import Books</button>
      <p class="format-hint">Supports: txt, epub</p>

      <!-- 隐藏的文件输入框，用于选择文件 -->
      <input
          type="file"
          ref="fileInput"
          style="display: none"
          @change="handleFileSelect"
          accept=".txt, .epub"
      />
    </div>
  </header>
</template>

<script>
export default {
  name: 'BookshelfHeader',
  methods: {
    // 点击导入书籍按钮时，触发文件选择器
    importBooks() {
      this.$refs.fileInput.click(); // 手动触发文件选择器
    },
    // 处理文件选择
    async handleFileSelect(event) {
      const file = event.target.files[0]; // 获取用户选择的文件
      if (!file) {
        alert('No file selected');
        return;
      }

      // 创建 FormData 来处理文件上传
      const formData = new FormData();
      formData.append('file', file);

      try {
        // 发送 POST 请求，将文件上传至后端
        const response = await fetch('http://localhost:5000/api/save_book', {
          method: 'POST',
          body: formData, // 发送文件数据
        });

        const result = await response.json();
        if (response.ok) {
          alert(result.message); // 成功提示
          // 在成功上传文件后，可以刷新页面或其他操作
        } else {
          alert(result.message); // 错误提示
        }
      } catch (error) {
        console.error('Error saving the book:', error);
        alert('Failed to save the book.'); // 网络或其他错误提示
      }
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
