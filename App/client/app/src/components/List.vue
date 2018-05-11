<template>
  <v-parallax :src="`http://p0s30qphu.bkt.clouddn.com/18-1-8/${ mainparallax.url }.jpg`" height="1000">
    <v-content class="px-0 py-0">
      <v-container fluid>
        <v-layout column>
          <v-flex xs12 sm6>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>节点列表</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>sort</v-icon>
              </v-btn>
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
              <v-card>
                <v-container fluid grid-list-md>
                  <v-layout row wrap>
                    <v-flex xs12 sm12>
                      <v-list two-line>
                        <template v-for="(item, index) in nodes">
                          <v-list-tile avatar ripple @click="openDialog(item)" :key="item.title">
                            <v-list-tile-content>
                              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                              <v-list-tile-sub-title>{{ item.transfer }}</v-list-tile-sub-title>
                            </v-list-tile-content>
                            <v-list-tile-action>
                              <v-icon color="red" v-if="item.statu==='0'">error</v-icon>
                              <v-icon color="yellow darken-2" v-else-if="item.statu==='1'">report_problem</v-icon>
                              <v-icon color="green" v-else>cloud_done</v-icon>
                            </v-list-tile-action>
                          </v-list-tile>
                          <v-divider v-if="index + 1 < nodes.length" :key="index"></v-divider>
                        </template>
                      </v-list>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card>
              <template id="modal">
                <v-dialog v-model="dialog" max-width="500">
                  <v-card>
                    <v-card-media :src="`http://p0s30qphu.bkt.clouddn.com/17-12-11//${ node.pic }.jpg`" height="400px"></v-card-media>
                    <v-card-title class="headline">{{ node.title }}</v-card-title>
                    <v-card-text>{{ node.transfer }}</v-card-text>
                  </v-card>
                </v-dialog>
              </template>
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
      dialog: false,
      loaded: false,
      nodes: [
        { id: '', title: '节点名称', transfer: "流量", statu: "0", pic: "63455021" },
        { id: '', title: '节点名称', transfer: "流量", statu: "1", pic: "63455021" },
        { id: '', title: '节点名称', transfer: "流量", statu: "2", pic: "63455021" },
        { id: '', title: '节点名称', transfer: "流量", statu: "0", pic: "63455021" },
        { id: '', title: '节点名称', transfer: "流量", statu: "1", pic: "63455021" },
        { id: '', title: '节点名称', transfer: "流量", statu: "2", pic: "63455021" }
      ],
      node: {
        id: null,
        title: null,
        transfer: null,
        statu: null,
        pic: null
      },
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
      this.error = this.nodes = null
      this.loaded = false
      this.axios.get('http://localhost:8843/').then((response) => {
        if (response.status == 200) {
          if (response.data.error) {
            this.error = response.error.toString()
          } else {
            if (response.data.empty) {
              this.empty = true
            } else {
              this.nodes = response.data.nodes
            }
            this.mainparallax = response.data.mainparallax
          }
          this.loaded = true
        } else {
          this.error = response.statusText
        }
      })
    },
    openDialog(item) {
      this.node = item
      this.dialog = true
    }
  },
  name: 'List'
}

</script>
