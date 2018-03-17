Vue.use(VueRouter);

const List =() => import('./component/list.vue')
const SpeedTest = () => import('./component/testspeed.vue')
const Tips =() =>  import('./component/tips.vue')
const Setting =() =>  import('./component/setting.vue')
const Usage =() =>  import('./component/usage.vue')


const routes = [
  { path: '/list', component: List },
  { path: '/speedtest', component: SpeedTest }, 
  { path: '/tips', component: Tips },
  { path: '/setting', component: Setting },
  { path: '/usage', component: Usage },
  { path: '*', redirect: '/list' }
]

const router = new VueRouter({
  routes: routes
})

const app = new Vue({
  router: router, 
  data: () => ({
      dialog: false,
      drawer: null,
      user: {
        head: '24935690',
        name: 'Delitto'
      },
      nodes: [
        { icon: 'list', text: '节点列表', url: '/list' },
        { icon: 'trending_up', text: '节点测速', url:'/speedtest' },
        { icon: 'help', text: '使用教程', url:'/tips' }
      ],
      users: [
        { icon: 'settings', text: '用户设置', url:'setting', url: 'setting' },
        { icon: 'data_usage', text: '使用情况', url:'usage', url: 'usage' }
        
      ]
    }),
    props: {
      source: String
    },
    
}).$mount('#app')