<template>
  <div class="chat-icon" @click="toggleSidebar">
    <!-- Replace with your actual chat icon -->
    <i class="fas fa-comments"></i>
  </div>
</template>
  
  <script>
export default {
  methods: {
    toggleSidebar() {
      this.$emit("toggle");
    },
  },
};
</script>
  
  <style scoped>
/* Add your chat box styles here */
.chat-icon {
  position: fixed;
  bottom: 40px;
  right: 20px;
  cursor: pointer;
  z-index: 1000;
}

.chat-icon .fas {
  font-size: 30px;
}
</style>
  