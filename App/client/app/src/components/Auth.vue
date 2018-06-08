<template>
<v-parallax :src="`https://ib.delitto.club/images/2018/06/07/0dV.jpg`" height="1000">
  <v-content class="px-0">
    <v-container fluid fill-height>
      <v-layout  justify-center>
        <v-flex xs12 sm12 md12>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title v-if="login">登录</v-toolbar-title>
              <v-toolbar-title v-if="!login">注册</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip right v-if="login">
                <v-btn slot="activator" icon large @click.native="login = !login">
                  <v-icon large>arrow_forward</v-icon>
                </v-btn>
                <span>注册</span>
              </v-tooltip>
              <v-tooltip right v-if="!login">
                <v-btn slot="activator" icon large @click.native="login = !login">
                  <v-icon large>arrow_back</v-icon>
                </v-btn>
                <span>登录</span>
              </v-tooltip>
            </v-toolbar>
            <v-card-text>
              <v-form ref="form" v-model="form">
                <v-text-field 
                  v-model="u"
                  v-if="login" 
                  prepend-icon="person" 
                  name="login" 
                  label="邮箱" 
                  type="text" 
                  :rules="emailRules"
                  ></v-text-field>
                <v-text-field 
                  v-model="u"
                  v-if="!login" 
                  prepend-icon="person" 
                  name="regist" 
                  label="邮箱" 
                  type="text" 
                  :rules="emailRules"
                  ></v-text-field>
                <v-text-field 
                  v-model="p"
                  id="password" 
                  prepend-icon="lock" 
                  name="password" 
                  label="密码" 
                  type="password" 
                  :rules="noEmpty"
                  ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn v-if="login" color="primary" @click.native="log()">登录</v-btn>
              <v-btn v-if="login" color="primary lighten-1" @click.native="tempLog()">访客登录</v-btn>
              <v-btn v-if="!login" flat @click.native="regist()"></v-btn>
              <v-tooltip left v-if="!login">
                <v-btn slot="activator" icon >
                  <v-icon large>help</v-icon>
                </v-btn>
                <span>找不到注册按钮？好好想想不加钱你能注册吗？</span>
              </v-tooltip>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
  <v-snackbar :color="snackbarColor" v-model="snackbar">{{ alertText }}</v-snackbar>
</v-parallax>
</template>

<script>
  import * as types from '@/store/types'
  export default {
    data: () => ({
      login: true,
      form: null,
      u: null,
      p: null, 
      snackbarColor: null,
      snackbar: null,
      alertText: '',
      noEmpty: [
        v => !!v || "不能为空"
      ],
      emailRules: [
        v => !!v || "不能为空",
        v => /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$/.test(v) || /^Delitto$/.test(v) || "格式不正确",

      ]
    }),
    methods: {
      log() {
        if(this.$refs.form){
          if(this.$refs.form.validate()){
            this.axios.post('/api/auth/login', {
              username: this.u,
              password: this.p
            }).then((response) => {
              if (response.status == 200){
                if(response.data.retCode == 0) {
                  this.alertText = '登录失败'
                  this.snackbarColor = 'error'
                  this.snackbar = true
                }else{
                  this.$store.commit(types.LOGIN, response.data.token)
                  this.$router.push({
                    path: '/list'
                  })
                }
              } else{
                this.alertText = '服务器异常'
                this.snackbarColor = 'error'
                this.snackbar = true
              }
            })
            .catch(() => {
              this.alertText = '网络异常'
              this.snackbarColor = 'error'
              this.snackbar = true
            })
          }
        }
      },
      tempLog() {
        this.axios.post('/api/auth/temp')
        .then((response) => {
          if (response.status == 200) {
            if (response.data.retCode == 1){
              this.$store.commit(types.LOGIN, response.data.token)
              this.$router.push({
                path: '/list'
              })

            }else{
              this.alertText = '不欢迎非洲人，谢谢'
              this.snackbarColor = 'error'
              this.snackbar = true
            }
          }else{
            this.alertText = '服务器异常'
            this.snackbarColor = 'error'
            this.snackbar = true
          }
        })
        .catch(() => {
          this.alertText = '网络异常'
          this.snackbarColor = 'error'
          this.snackbar = true
        })
      },
      regist() {
        if(this.$refs.form){
          if(this.$refs.form.validate()){
            this.axios.post('/api/auth/register',{
              'username': this.u,
              'password': this.p,
              'invitecode': 'Delitto'
            }).then((response) => {
              if(response.status == 200){
                this.$store.commit(types.LOGIN, response.data.token)
                  this.$router.push({
                    path: '/list'
                })
              } else {
                this.alertText = '服务器异常'
                this.snackbarColor = 'error'
                this.snackbar = true
              }
            }).catch(() => {
              this.alertText = '网络异常'
              this.snackbarColor = 'error'
              this.snackbar = true
            })
          }
        }
      }
    },
    created() {
      if (this.$store.state.loged) {
        this.$router.push({
          path: '/list'
        })
      }
    },
    name: 'Auth'
  }
</script>