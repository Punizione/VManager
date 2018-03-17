<template>
 <v-app>
    <v-navigation-drawer
      fixed
      clipped
      app
      v-model="drawer"
      floating
      value="true"
    >
      <v-card
        flat
      >
        <v-card-media
          :src="`http://p0s30qphu.bkt.clouddn.com/18-1-8//${user.head}.jpg`"
          height="200px"
        >
        </v-card-media>
        <v-card-title primary-title>
         
            <v-layout
              justify-center
            >
                <div class="headline">{{ user.name }}</div> 
            </v-layout>
        </v-card-title>
      </v-card>
      <v-list dense>
        <v-subheader class="mt-3 grey--text text--darken-1">NODES</v-subheader>

        <v-list-tile v-for="item in nodes" :key="item.text" :to="{ path: item.url }">
          
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          
          <v-list-tile-content>
            
            <v-list-tile-title>
              <span>{{ item.text }}</span>
            </v-list-tile-title>
            
          </v-list-tile-content>
          
         
        </v-list-tile>
        </v-list>
        <v-list dense>
        <v-subheader class="mt-3 grey--text text--darken-1">USER</v-subheader>
        <v-list-tile v-for="item in users" :key="item.text" :to="{ path: item.url }">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>
              {{ item.text }}
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar
      color="blue darken-3"
      dark
      app
      :clipped-left="$vuetify.breakpoint.mdAndUp"
      fixed
    >
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-sm-and-down">VManager</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        prepend-icon="search"
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>notifications</v-icon>
      </v-btn>
      <v-btn icon large>
        <v-avatar size="32px" tile>
          <img
            src="https://vuetifyjs.com/static/doc-images/logo.svg"
            alt="Vuetify"
          >
        </v-avatar>
      </v-btn>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center align-center>
         
        <v-fade-transition mode="out-in">
          <router-view></router-view>
        </v-fade-transition>
   
          
        </v-layout>
      </v-container>
    </v-content>
    <v-btn
      fab
      bottom
      right
      color="pink"
      dark
      fixed
      @click.stop="dialog = !dialog"
    >
      <v-icon>add</v-icon>
    </v-btn>
    
  </v-app>
</template>

<script>
export default {
 data: () => ({
      dialog: false,
      drawer: null,
      user: {
        head: '24935690',
        name: 'Delitto'
      },
      nodes: [
        { icon: 'list', text: '节点列表', url: '/list' },
        { icon: 'trending_up', text: '节点测速', url:'/speedtest' },
        { icon: 'help', text: '使用教程', url:'/tips' }
      ],
      users: [
        { icon: 'settings', text: '用户设置', url:'setting', url: 'setting' },
        { icon: 'data_usage', text: '使用情况', url:'usage', url: 'usage' }
        
      ]
    }),
    props: {
      source: String
    },
  name: 'App'
}
</script>
