import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import './assets/tailwind.css'

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)     // inyeccion de Pinia
app.mount('#app')