import axios from 'axios'
import store from '@/store/store'
import * as types from '@/store/types'
import router from '@/router/index'


axios.defaults.timeout = 5000
//axios.defaults.baseURL = 'http://localhost:5000'

const downloadUrl = url => {
	let iframe = document.createElement('iframe')
	iframe.style.display = 'none'
	iframe.src = url
	iframe.onload = function() {
		document.body.removeChild(iframe)
	}
	document.body.appendChild(iframe)
}
axios.interceptors.request.use(
	config => {
		if (store.state.token){
			config.headers.Authorization = `token ${store.state.token}`;
		}
		return config
	},
	err => {
		return Promise.reject(err)
	}
);

axios.interceptors.response.use(
	response => {
		if (response.headers && response.headers['content-type'] == 'application/octet-stream') {
			downloadUrl(response.request.responseURL)
			return
		}
		return response
	},
	error => {
		if(error.response){
			switch(error.response.status){
				case 401:
					store.commit(types.LOGOUT);
					router.replace({
						path: 'auth'
					})
			}
		}
		return Promise.reject(error)
	}
);

export default axios