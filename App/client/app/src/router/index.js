import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store/store'
import * as types from '@/store/types'
import List from '@/components/List'
import Setting from '@/components/Setting'
import SpeedTest from '@/components/SpeedTest'
import Tips from '@/components/Tips'
import Rss from '@/components/Rss'
import Download from '@/components/Download'
import Auth from '@/components/Auth'

Vue.use(Router)


if(window.localStorage.getItem('token')){
	store.commit(types.LOGIN, window.localStorage.getItem('token'))
}

const router = new Router({
  routes: [
      { 
      	path: '/list', 
      	component: List,
      	name: '/list',
      	meta: {
      		requireAuth: true
      	} 
      },
	  { 
	  	path: '/speedtest', 
	  	component: SpeedTest,
	  	name: '/speedtest',
	  	meta: {
	  		requireAuth: true
	  	} 
	  }, 
	  { 
	  	path: '/tips', 
	  	component: Tips,
	  	name: '/tips',
	  	meta: {
	  		requireAuth: true
	  	} 
	  },
	  { 
	  	path: '/setting', 
	  	component: Setting,
	  	name: '/setting',
	  	meta: {
	  		requireAuth: true
	  	} 
	  },
	  { 
	  	path: '/rss', 
	  	component: Rss,
	  	name: '/rss',
	  	meta: {
	  		requireAuth: true
	  	} 
	  },
	  { 
	  	path: '/download',
	  	component: Download,
	  	name: '/download',
	  	meta: {
	  		requireAuth: true
	  	} 
	  },
	  {
	  	path: '/auth',
	  	component: Auth,
	  	name: '/auth'
	  }
  ]
});

router.beforeEach((to, from, next) => {
	if (to.matched.some(r => r.meta.requireAuth)) {
		if(store.state.token){
			next();
		}else{
			next({
				path: '/auth'
			});
		}
	} else{
		next();
	}
})
export default router;