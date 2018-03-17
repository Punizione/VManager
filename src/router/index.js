import Vue from 'vue'
import Router from 'vue-router'
import List from '@/components/List'
import Setting from '@/components/Setting'
import SpeedTest from '@/components/SpeedTest'
import Tips from '@/components/Tips'
import Usage from '@/components/Usage'

Vue.use(Router)

export default new Router({
  routes: [
     { path: '/list', component: List },
	  { path: '/speedtest', component: SpeedTest }, 
	  { path: '/tips', component: Tips },
	  { path: '/setting', component: Setting },
	  { path: '/usage', component: Usage },
	  { path: '*', redirect: '/list' }
  ]
})
