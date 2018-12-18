import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import Menu from '../components/Menu.vue'
import Login from '../components/Login.vue'
import Burgers from '../components/Burgers.vue'
import Shakes from '../components/Shakes.vue'
import Salads from '../components/Salads.vue'
import Pastas from '../components/Pastas.vue'
import Beverages from '../components/Beverages.vue'
import Cart from '../components/Cart.vue'
import User from '../components/User.vue'
import Register from '../components/Register.vue'
import Welcome from  '../components/Welcome.vue'

Vue.use(Router)

export default new Router({
  mode : 'history',
  routes : [
    {
      path: '/',
      component: Welcome
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/register',
      component: Register
    },
    {
      path:'/menu',
      component: Menu,
      children:[
        { path: 'burgers', component: Burgers },
        { path: 'shakes', component: Shakes },
        { path: 'salads', component: Salads },
        { path: 'pastas', component: Pastas },
        { path: 'beverages', component: Beverages }
      ]
    },
    {
      path:'/cart',
      component:Cart
    },
    {
      path:'/user',
      component:User
    }
  ]
})
