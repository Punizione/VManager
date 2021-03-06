// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'
import Vuetify from 'vuetify'
import store from './store/store'

import axios from './utils/http'
import VueAxios from 'vue-axios'
import Aplayer from 'vue-aplayer'
import QRCode from 'qrcode'

Vue.use(VueAxios, axios)

import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
