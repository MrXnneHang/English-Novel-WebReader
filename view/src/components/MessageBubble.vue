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
    text(newVal, oldVal) {
      // 只有当新的 text 不为空且与旧的 text 不同时，才触发 showMessage
      if (newVal && newVal !== oldVal) {
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
    },
    forceShowMessage() {
      // 即使 text 没有改变，手动调用时也强制显示消息
      this.showMessage();
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
  overflow: hidden; /* 防止溢出 */
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
  max-height: 240px;  /* 控制内容区域的最大高度 */
  overflow-y: auto;   /* 内容滚动 */
  white-space: pre-wrap; /* 保留换行符 */
  word-break: break-word; /* 防止长单词溢出 */
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
