import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Create.vue'
import login from '../components/login.vue'

const routes = [
  {
    path: '/create',
    name: 'Create',
    component: Home
  },
  {
    path: '/attacks',
    name: 'Attacks',
    component: () => import('../views/Attacks.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: login
  },
  {
    path: '/',
    name: 'Search',
    component: () => import('../views/search.vue')
  },
  {
    path: '/visual',
    name: 'Visualization',
    component: () => import('../views/visualization.vue')
  },
  {
    path: '/filecreate',
    name: 'FileCreate',
    component: () => import('../views/FileCreate.vue')
  },
]
const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
