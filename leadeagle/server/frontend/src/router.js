import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Ping from '@/components/Ping';
import Upload from '@/components/Upload';
import Dataset from '@/components/Dataset';
import Projects from '@/components/Projects';

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/tiles',
      name: 'tiles',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import( /* webpackChunkName: "tiles" */ './views/Tiles.vue')
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload,
    },
    {
      path: '/datasets',
      name: 'Dataset',
      component: Dataset,
    },
    {
      path: '/projects',
      name: 'Projects',
      component: Projects,
    },
  ]
})