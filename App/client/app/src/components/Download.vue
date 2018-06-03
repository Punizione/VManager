<template>
  <v-parallax src="http://p0s30qphu.bkt.clouddn.com/18-1-8/13633991.jpg" height="1000">
    <v-content class="px-0 py-0">
      <v-container fluid>
        <v-layout column>
          <v-flex xs12 sm6>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>资源下载</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>sort</v-icon>
              </v-btn>
            </v-toolbar>
            <v-container fluid grid-list-lg>
              <v-layout row wrap>
                <template v-for="item in resources">
                  <v-flex xs12 sm6 lg4>
                    <v-card  :key="item.title">
                      <v-container fluid>
                        <v-layout row wrap>
                          <v-flex xs5>
                            <v-card-media src="@/assets/1.png" height="125px" contain></v-card-media>
                          </v-flex>
                          <v-flex xs7>
                            <div>
                              <div class="headline">{{ item.title }}</div>
                              <div>{{ item.text }}</div>
                            </div>
                          </v-flex>
                        </v-layout>
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <template v-for="(res, index) in item.res">
                            <v-btn color="primary" flat slot="activator" @click="showVerify(res.src)">下载链接{{ index+1 }}</v-btn>
                          </template>
                        </v-card-actions>
                      </v-container>
                    </v-card>
                  </v-flex>
                </template>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-dialog v-model="verifyDialog" max-width="290">
      <v-card>
        <v-card-title class="headline">下载验证</v-card-title>
        <v-container>
          <v-layout row wrap>
            <v-flex xs12>
              <v-card-media :src="verifyCode" @click.native="loadVerifyCode()" height="200px"></v-card-media>
            </v-flex>
            <v-flex xs12>
            <v-form ref="verifyCode">
              <v-text-field  label="请输入上图标准分子式" :loading="progress" v-model="code" :rules="noEmptyRules">
                  <v-progress-linear  :indeterminate="true" height="2" slot="progress"></v-progress-linear>
              </v-text-field>
              </v-form>
            </v-flex>
          </v-layout>
        </v-container>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" flat @click.native="loadVerifyCode()">更换验证图片</v-btn>
          <v-btn color="primary" flat @click.native="verify()">验证</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar :color="snackbarColor" v-model="snackbar" right bottom>{{ alertText }}</v-snackbar>
  </v-parallax>
</template>
<script>
export default {
  data : () => ({
    snackbarColor: "success",
    snackbar: null,
    alertText: '',
    verifyDialog: false,
    verifyCode: '',
    h: '',
    code: null,
    progress: false,
    downloadLink: null,
    noEmptyRules: [
        v => !!v || "不能为空"
      ],
    resources : [
      { title: "SSR-Anndroid", text: "4.7.1", icon: "", res:[ {src: "https://xx.yy"},{src: "https://xx.yy"},{src: "https://xx.yy"}] },
      { title: "SSR-Anndroid", text: "4.7.1", icon: "", res:[ {src: "https://xx.yy"},{src: "https://xx.yy"},{src: "https://xx.yy"}] },
      { title: "SSR-Anndroid", text: "4.7.1", icon: "", res:[ {src: "https://xx.yy"},{src: "https://xx.yy"},{src: "https://xx.yy"}] }
    ]
  }),
  watch: {
    verifyDialog: 'stopLoading'
  },
  methods:{
    showVerify(url) {
      this.verifyDialog = true
      this.downloadLink = url
      this.loadVerifyCode()
    },
    loadVerifyCode() {
      this.axios.get('/api/code')
        .then((response) => {
          if(response.status == 200){
            this.verifyCode = response.data.url
            this.h = response.data.h
          } else {
            this.alertText = '加载失败.webp'
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
    verify() {
      if(this.$refs.verifyCode){
        if(this.$refs.verifyCode.validate()){
          this.progress = true
          this.axios.post('/api/verify', {
            code: this.code,
            h: this.h
          }).then((response) => {
            if(response.status == 200){
              if(response.data.retCode == 1){
                  this.alertText = '验证成功'
                  this.snackbarColor = 'success'
                  this.snackbar = true
                  this.verifyDialog = false
                  this.axios.get(this.downloadLink).catch(() => {
                    this.alertText = '网络异常'
                    this.snackbarColor = 'error'
                    this.snackbar = true
                  })
              } else {
                  this.alertText = '验证失败'
                  this.snackbarColor = 'error'
                  this.snackbar = true
                  this.loadVerifyCode()
              }
            } else {
              this.alertText = '网络异常'
              this.snackbarColor = 'error'
              this.snackbar = true
            }
            this.stopLoading()
          })
        } 
      }
      
    },
    stopLoading() {
      if( this.progress ){
        this.progress = ! this.progress
      }
    }

  }
}
</script>