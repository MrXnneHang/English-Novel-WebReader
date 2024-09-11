<template>
  <div class="file-upload">
    <input type="file" @change="onFileChange" accept=".txt" />
  </div>
</template>

<script>
export default {
  props: {
    onFileChange: Function, // 从父组件接收上传文件时触发的方法
  },
};
</script>

<style scoped>
.file-upload {
  padding: 20px;
  background-color: #f8f8f8;
  text-align: center;
}
input[type="file"] {
  padding: 10px;
  font-size: 16px;
}
</style>
