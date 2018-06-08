<template>
  <v-parallax :src="`https://ib.delitto.club/images/2018/06/07/0dV.jpg`" height="1000">
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
                <template v-else>
                  <v-tab v-for="item in steps" :key="item.text">
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
                    <img src="https://ib.delitto.club/images/2018/06/07/82s.gif" />
                  </v-layout>
                </v-container>
              </v-content>
            </template>
            <template v-else>
              <v-tabs-items v-model="tab">
                <v-tab-item v-for="item in steps" :key="item.text">
                  <v-card>
                    <v-stepper v-model="steptor" vertical non-linear>
                      <template v-for="st in item.step">
                        <v-stepper-step :step='st.num' :complete='steptor > st.num' editable edit-icon="done">
                          <div class="headline">{{ st.title }}</div>
                          <small>{{ st.subtitle }}</small>
                        </v-stepper-step>
                        <v-stepper-content :step='st.num'>
                          <v-card  flat>
                            <v-card-media :src="st.pic" height="196" contain>
                            </v-card-media>
                            <v-card-title primary-title>
                              <div>{{ st.text }}</div>
                            </v-card-title>
                          </v-card>
                          <template v-if="st.num>1">
                            <v-btn flat @click.native="steptor = st.num-1">上一步</v-btn>
                          </template>
                          
                          <template v-if="st.num<item.step.length">
                            <v-btn color="primary" @click.native="steptor = st.num+1">下一步</v-btn>
                          </template>
                          <template v-else>
                            <v-btn color="primary" @click.native="steptor = 1">第一步</v-btn>
                          </template>
                        </v-stepper-content>
                      </template>
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
      steps: [{
          text: 'ssr',
          icon: 'airplanemode_active',
          step: null
        },
        {
          text: 'v2ray',
          icon: 'airplanemode_active',
          step:  null
        },
        {
          text: 'IPV6',
          icon: '6',
          step:  null
        },
        {
          text: 'SwitchyOmega',
          icon: '6',
          step:  null
        }
      ],
      empty: false,
      error: null,

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
      this.axios.get('/api/tips').then((response) => {
        if (response.status == 200) {
          this.steps = response.data.steps
          this.steptor = 1
          this.tab = '0'
          this.loaded = true
        } else {
          this.error = response.statusText
        }
      }).catch(() => {
        this.loaded = true
      })
    }
  },
  name: 'Tips'
}

</script>
