<template>
  <v-parallax src="http://p0s30qphu.bkt.clouddn.com/18-1-8/13633991.jpg" height="1000">
    <v-content class="px-0 py-0">
      <v-container fluid>
        <v-layout column>
          <v-flex xs12 sm6>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>用户订阅</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>sort</v-icon>
              </v-btn>
            </v-toolbar>
            <v-container fluid>
              <v-layout row>
                <v-flex xs12>
                  <v-card>
                    <v-container fluid>
                      <v-flex xs12>
                        SSR订阅: <span>{{ ssrRss }}</span>
                      </v-flex>
                      <v-flex xs12>
                        V2Ray订阅: <span>{{ v2rayRss }}</span>
                      </v-flex>
                      <v-flex xs12>
                        Bak1订阅: <span>{{ bak1Rss }}</span>
                      </v-flex>
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
  data : () => ({
    snackbarColor: "success",
    snackbar: null,
    alertText: '',
    ssrRss: 'https://xx.yy',
    v2rayRss: 'https://xx.yy',
    bak1Rss: 'https://xx.yy'

  }),
  created() {
    this.fetchData()
  },
  methods: {
    fetchData(){
      this.axios.get('/api/rss').then((response) => {
        if(response.status == 200){
          this.ssrRss = response.data.ssrRss
          this.v2rayRss = response.data.v2rayRss
          this.bak1Rss = response.data.bak1Rss
        }
      })
    }
  }
}
</script>
