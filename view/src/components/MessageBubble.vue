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
      <button class="save-button" @click="saveWord">Save Word/Sentence</button>
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
      isVisible: false,
      autoCloseTimer: null // 用于存储自动关闭定时器 ID
    };
  },
  watch: {
    text(newVal, oldVal) {
      if (newVal && newVal !== oldVal) {
        this.showMessage();
      }
    }
  },
  methods: {
    showMessage() {
      this.isVisible = true;

      // 清除之前的定时器，避免重复启动
      if (this.autoCloseTimer) {
        clearTimeout(this.autoCloseTimer);
      }

      // 设置新的定时器，在 10 秒后自动关闭消息气泡
      this.autoCloseTimer = setTimeout(() => {
        this.closeMessage();
      }, 10000); // 10 秒钟
    },
    closeMessage() {
      this.isVisible = false;

      // 清除定时器，防止自动关闭时已经关闭的消息气泡再次被触发
      if (this.autoCloseTimer) {
        clearTimeout(this.autoCloseTimer);
        this.autoCloseTimer = null;
      }
    },
    async saveWord() {
      try {
        const response = await fetch('http://localhost:5000/api/save_word', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          }
          // No body required for this request
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Word saved:', data.message);
        alert(data.message);

      } catch (error) {
        console.error('Error saving word:', error);
        alert('Error saving word.');
      }
    },
    forceShowMessage() {
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
  overflow: hidden;
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
  max-height: 240px;
  overflow-y: auto;
  white-space: pre-wrap;
  word-break: break-word;
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
