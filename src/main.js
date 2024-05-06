import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router'; // Import your Vue Router instance

const app = createApp(App);

app.use(router); // Use Vue Router with your Vue app

app.mount('#app');
