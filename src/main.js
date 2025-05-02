import { registerPlugins } from '@/plugins'

import App from './App.vue'

import "@/assets/css/app.css";
import '@/assets/fonts/fonts.css';

import { createApp } from 'vue'

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
