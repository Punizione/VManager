import Vuex from 'vuex'
import Vue from 'vue'
import * as types from '@/store/types'


Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		token: null,
		loged: false
	},
	mutations: {
		[types.LOGIN]: (state, data) => {
			localStorage.token = data
			state.token = data
			state.loged = true
		},
		[types.LOGOUT]: (state) => {
			localStorage.removeItem('token')
			state.token = null
			state.loged = false
		}
	}
})