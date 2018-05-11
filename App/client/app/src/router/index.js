import Vue from 'vue'
import Router from 'vue-router'
import List from '@/components/List'
import Setting from '@/components/Setting'
import SpeedTest from '@/components/SpeedTest'
import Tips from '@/components/Tips'
import Rss from '@/components/Rss'
import Download from '@/components/Download'

Vue.use(Router)

export default new Router({
  routes: [
     { path: '/list', component: List },
	  { path: '/speedtest', component: SpeedTest }, 
	  { path: '/tips', component: Tips },
	  { path: '/setting', component: Setting },
	  { path: '/rss', component: Rss },
	  { path: '/download', component: Download },
	  { path: '*', redirect: '/list' }
  ]
})
