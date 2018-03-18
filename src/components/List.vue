<template>
  <v-content>
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
          <v-card>
            <v-container fluid grid-list-md>
              <v-layout row wrap>
                <v-flex xs12 sm12>
                  <v-list two-line>
                    <template v-for="(item, index) in nodes">
                      <v-list-tile avatar ripple @click="toggle(index)" :key="item.title">
                        <v-list-tile-content>
                          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                          <v-list-tile-sub-title>{{ item.subtitle }}</v-list-tile-sub-title>
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
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>
<script>
export default {
  data() {
    return {
      loaded: false,
      nodes: [
        { title: '节点名称', subtitle: "流量", statu: "0" },
        { title: '节点名称', subtitle: "流量", statu: "1" },
        { title: '节点名称', subtitle: "流量", statu: "2" },
        { title: '节点名称', subtitle: "流量", statu: "0" },
        { title: '节点名称', subtitle: "流量", statu: "1" },
        { title: '节点名称', subtitle: "流量", statu: "2" }
      ],
      empty: false,
      error: null
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
