import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import HelloWorld from "../components/HelloWorld.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '',
      name: 'home',
      component: HelloWorld
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})

export default router