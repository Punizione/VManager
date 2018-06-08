<template>
  <v-parallax src="https://ib.delitto.club/images/2018/06/07/0dV.jpg" height="1000">
    <v-content class="px-0 py-0">
      <v-container fluid>
        <v-layout column>
          <v-flex xs12 sm6>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>用户设置</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>sort</v-icon>
              </v-btn>
            </v-toolbar>
            <v-container fluid>
              <v-layout row>
                <v-flex xs12 sm6>
                  <v-card>
                    <v-container fluid>
                      <v-card-title><h3 class="headline">修改密码</h3></v-card-title>
                      <v-form v-model="changePswForm" ref="changePswForm" lazy-validation>
                        <v-flex xs12>
                          <v-text-field 
                            v-model="oldPassword" 
                            label="原密码" 
                            :rules="noEmpty" 
                            required 
                            :append-icon="e1 ? 'visibility_off' : 'visibility'" 
                            :append-icon-cb="() => (e1 = !e1)" 
                            :type="e1?'password':'text'"
                          ></v-text-field>
                        </v-flex>
                        <v-flex xs12>
                          <v-text-field 
                            v-model="newPassword" 
                            label="新密码" 
                            :rules="noEmpty" 
                            required
                            :append-icon="e2 ? 'visibility_off' : 'visibility'" 
                            :append-icon-cb="() => (e2 = !e2)" 
                            :type="e2?'password':'text'"
                          ></v-text-field>
                        </v-flex>
                        <v-flex xs12>
                          <v-text-field 
                            v-model="newPasswordRe" 
                            label="新密码again" 
                            :rules="noEmpty" 
                            required
                            :append-icon="e3 ? 'visibility_off' : 'visibility'" 
                            :append-icon-cb="() => (e3 = !e3)" 
                            :type="e3?'password':'text'"
                          ></v-text-field>
                        </v-flex>
                      </v-form>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn flat color="orange" @click.native="changePassword()">修改</v-btn>
                      </v-card-actions>
                    </v-container>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-snackbar :color="snackbarColor" v-model="snackbar" right bottom>{{ alertText }}</v-snackbar>
  </v-parallax>

</template>
<script>
export default {
  data: () => ({
    snackbarColor: 'primary',
    snackbar: null,
    alertText: '',
    e1: true,
    e2: true,
    e3: true,
    changePswForm: null,
    oldPassword: null,
    newPassword: null,
    newPasswordRe: null,

    noEmpty: [
      v => !!v || "不能为空"
    ]
  }),
  methods: {
    changePassword() {
      if(this.$refs.changePswForm.validate()){
        if(this.newPassword == this.newPasswordRe){
          this.axios.post('/api/user',{
            'p1': this.oldPassword,
            'p2':this.newPassword
          }).then((response) => {
            if(response.status==200){
              if(response.data.retCode == 0) {
                this.snackbarColor = 'success'
                this.alertText = '修改成功'
              } else if(response.data.retCode == -1){
                this.snackbarColor = 'warning'
                this.alertText = '原密码错误'
              } else {
                this.snackbarColor = 'error'
                this.alertText = '你个游客改个P的密码'
              }
            }else{
              this.snackbarColor = 'error'
              this.alertText = '网络异常'
            }
          })
        } else {
          this.snackbarColor = 'error'
          this.alertText = '两次输入密码不一致'
        }
        this.snackbar = true
      }
    }

  }

}
</script>
