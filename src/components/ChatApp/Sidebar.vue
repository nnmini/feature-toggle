<template>
  <div class="sidebar-pane">
    <div class="chat-messages">
      <!-- Display chat messages -->
      <div v-for="(message, index) in messages" :key="index">
        {{ message }}
      </div>
    </div>
    <div class="input-container">
      <input
        v-model="inputMessage"
        type="text"
        placeholder="Enter your question"
        class="chat-input-text"
        @keyup.enter="sendMessage"
      />
    </div>
  </div>
</template>
  
  <script>
import axios from "axios";

export default {
  data() {
    return {
      inputMessage: "",
      messages: [],
    };
  },
  methods: {
    sendMessage() {
      this.messages.push(this.inputMessage);
      axios
        .post("http://localhost:5000/process_user_input", {
          user_input: this.inputMessage,
        })
        .then((response) => {
          console.log("response...", response);
          this.messages.push(response.data);
          this.$emit("response-received", response.data);
        })
        .catch((error) => {
          console.error("Error processing user input:", error);
        });
    },
  },
};
</script>
  
  <style scoped>
/* Add your sidebar styles here */
.sidebar-pane {
  background-color: #f4f4f4;
  width: 350px;
  display: flex;
  flex-direction: column;
}

.chat-messages {
  padding: 10px;
  flex: 1;
  overflow-y: auto;
}

.input-container {
  position: relative;
}

.chat-input-text {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
  