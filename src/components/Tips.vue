<template>
  <v-parallax :src="`http://p0s30qphu.bkt.clouddn.com/18-1-8/${ mainparallax.url }.jpg`" height="1000">
    <v-content class="px-0 py-0">
      <v-container fluid>
        <v-layout column>
          <v-flex xs12 sm12>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>使用教程</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>help</v-icon>
              </v-btn>
              <v-tabs color="indigo" slot="extension" v-model="tab" drak grow icons-and-text>
                <v-tabs-slider color="yellow"></v-tabs-slider>
                <template class="loading" v-if="loaded===false"></template>
                <template v-else-if="error" class="error"></template>
                <template v-else-if="empty" class="empty"></template>
                <template v-else>
                  <v-tab v-for="item in steps" :key="item">
                    {{ item.text }}
                    <v-icon>{{ item.icon }}</v-icon>
                  </v-tab>
                </template>
              </v-tabs>
            </v-toolbar>
            <template class="loading" v-if="loaded===false">
              <v-content class="px-0">
                <v-container>
                  <v-layout row justify-center align-center>
                    <img src="http://p0s30qphu.bkt.clouddn.com/18-3-18/77660072.jpg" />
                  </v-layout>
                </v-container>
              </v-content>
            </template>
            <template v-else-if="error" class="error"></template>
            <template v-else-if="empty" class="empty"></template>
            <template v-else>
              <v-tabs-items v-model="tab">
                <v-tab-item v-for="item in steps" :key="item.text">
                  <v-card>
                    <v-stepper v-model="steptor" vertical non-linear>
                      <v-stepper-step step="1" :complete="steptor > 1" editable edit-icon="done">
                        Select an app
                        <small>Summarize if needed</small>
                      </v-stepper-step>
                      <v-stepper-content step="1">
                        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
                        <v-btn color="primary" @click.native="steptor = 2">Continue</v-btn>
                        <v-btn flat>Cancel</v-btn>
                      </v-stepper-content>
                      <v-stepper-step step="2" :complete="steptor > 2" editable edit-icon="done">Configure analytics for this app</v-stepper-step>
                      <v-stepper-content step="2">
                        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
                        <v-btn color="primary" @click.native="steptor = 3">Continue</v-btn>
                        <v-btn flat>Cancel</v-btn>
                      </v-stepper-content>
                      <v-stepper-step step="3" :complete="steptor > 3" editable edit-icon="done">Select an ad format and name ad unit</v-stepper-step>
                      <v-stepper-content step="3">
                        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
                        <v-btn color="primary" @click.native="steptor = 4">Continue</v-btn>
                        <v-btn flat>Cancel</v-btn>
                      </v-stepper-content>
                      <v-stepper-step step="4" editable edit-icon="done">View setup instructions</v-stepper-step>
                      <v-stepper-content step="4">
                        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
                        <v-btn color="primary" @click.native="steptor = 1">Continue</v-btn>
                        <v-btn flat>Cancel</v-btn>
                      </v-stepper-content>
                    </v-stepper>
                  </v-card>
                </v-tab-item>
              </v-tabs-items>
            </template>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-parallax>
</template>
<script>
export default {
  data() {
    return {
      steptor: 1,
      tab: null,
      loaded: false,
      steps: [
        { text: 'ssr', icon: 'airplanemode_active' },
        { text: 'v2ray', icon: 'airplanemode_active' },
        { text: 'IPV6', icon: '6' },
        { text: 'SwitchyOmega', icon: '6' }
      ],
      empty: false,
      error: null,
      mainparallax: {
        url: null
      }
    }
  },
  created() {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData() {
      this.error = this.steps = null
      this.loaded = false
      this.axios.get('http://localhost:8843/steps').then((response) => {
        if (response.status == 200) {
          if (response.data.error) {
            this.error = response.error.toString()
          } else {
            if (response.data.empty) {
              this.empty = true
            } else {
              this.steps = response.data.steps
              this.steptor = 1

            }
            this.mainparallax = response.data.mainparallax
          }
          this.loaded = true
        } else {
          this.error = response.statusText
        }
      })
    }
  },
  name: 'List'
}

</script>
