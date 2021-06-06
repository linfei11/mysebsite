import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import installElementPlus from './plugins/element'
import './assets/css/global.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

axios.defaults.baseURL = 'http://localhost:8001'
const app = createApp(App)
installElementPlus(app)
app.use(VueAxios, axios)
app.use(router).mount('#app')
