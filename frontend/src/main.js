import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://212.101.137.104:8000/';  // the FastAPI backend

createApp(App).mount('#app')
