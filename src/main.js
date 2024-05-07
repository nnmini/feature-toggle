import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router'; // Import your Vue Router instance
import 'vuetify/styles';
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { store } from './store';
const app = createApp(App);

console.log("store...", store)
const vuetify = createVuetify({
    components,
    directives
})


app.use(router) // Use Vue Router with your Vue app
    .use(vuetify)
    .use(store)
    .mount('#app');
