<template>
  <div v-if="isVisible" class="message-bubble">
    <div class="message-header">
      <span>Message</span>
      <button class="close-button" @click="closeMessage">x</button>
    </div>
    <div class="message-content">
      {{ text }}
    </div>
    <div class="message-actions">
      <button class="save-button" @click="saveWord">Save Word</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      isVisible: false, // 初始状态为 false，只有当 text 存在时显示
      timer: null // 用于存储计时器 ID
    };
  },
  watch: {
    text(newVal) {
      if (newVal) {
        this.showMessage();
      }
    }
  },
  methods: {
    showMessage() {
      this.isVisible = true;
      // 清除之前的计时器，避免重复启动
      if (this.timer) {
        clearTimeout(this.timer);
      }
      // 自动关闭定时器
      this.timer = setTimeout(() => {
        this.isVisible = false;
      }, 10000); // 10秒后自动关闭
    },
    closeMessage() {
      this.isVisible = false;
      // 手动关闭时，清除计时器
      if (this.timer) {
        clearTimeout(this.timer);
      }
    },
    saveWord() {
      // 模拟保存功能，你可以在这里执行任何想要的保存逻辑
      console.log('Word saved:', this.text);
      alert('Word saved: ' + this.text);
    }
  }
}
</script>

<style scoped>
.message-bubble {
  position: fixed;
  top: 10px;
  right: 10px;
  width: 400px;
  height: 300px;
  background-color: #f8f9fa;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  z-index: 1000;
  overflow-y: auto;  /* 添加垂直滚动条 */
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.close-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

.message-content {
  max-height: 240px;  /* 控制内容区域的最大高度，避免超出 */
  overflow-y: auto;   /* 内容滚动 */
}

.message-actions {
  margin-top: 10px;
}

.save-button {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 3px;
  cursor: pointer;
}

.save-button:hover {
  background-color: #218838;
}
</style>
