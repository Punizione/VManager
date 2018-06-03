<template>
  <v-app>
    <v-navigation-drawer fixed clipped app v-model="drawer" floating value="true">
      <v-card flat>
        <v-card-media :src="`http://p0s30qphu.bkt.clouddn.com/18-1-8//${user.head}.jpg`" height="200px">
        </v-card-media>
        <v-card-title primary-title>
          <v-layout justify-center>
            <div class="headline">{{ user.name }}</div>
          </v-layout>
        </v-card-title>
      </v-card>
      <template v-for="menu in menus">
        <v-list dense :key="menu.title">
          <v-subheader class="mt-3 grey--text text--darken-1">{{ menu.title }}</v-subheader>
          <v-list-tile v-for="item in menu.items" :key="item.text" :to="{ path: item.url }">
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
      </template>
    </v-navigation-drawer>
    <v-toolbar color="blue darken-3" dark app :clipped-left="$vuetify.breakpoint.mdAndUp" fixed>
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-sm-and-down">VManager</span>
      </v-toolbar-title>
      <v-text-field flat solo-inverted prepend-icon="search" label="Search" class="hidden-sm-and-down"></v-text-field>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
      <v-bottom-sheet inset>
        <v-btn icon slot="activator">
          <v-icon>music_note</v-icon>
        </v-btn>
        
          <aplayer autoplay :music="defaultMusic" :list="musicList" />
        
      </v-bottom-sheet>
      <template v-if="loged">
      <v-menu transition="slide-x-transition" bottom left offset-y min-width="160px" >
        <v-btn icon large slot="activator">
          <v-avatar size="32px" tile>
            <img src="http://p0s30qphu.bkt.clouddn.com/18-3-18/26003829.jpg" alt="Vmanager">
          </v-avatar>
        </v-btn>
        <v-list>
          <v-list-tile @click="logout()">
            <v-list-tile-title>登出</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
      </template>
    </v-toolbar>
    <v-content>
      <v-container fluid class="px-0 py-0">
        <v-layout class="px-0 py-0">
          <v-flex xs12>
            <v-fade-transition mode="out-in">

              <router-view class="px-0 py-0" v-if="isRouterAlive"></router-view>
            </v-fade-transition>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
      <v-btn fab bottom right hover color="pink" dark fixed @click.stop="dialog = true" v-if="loged">
        <v-icon>add</v-icon>
      </v-btn>
    <v-dialog v-model="dialog" max-width="500px">
        <v-card>
          <v-card-title primary-title>
            新增节点
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-layout row wrap>
                <v-flex xs8 offset-xs2>
                  <v-container>
                    <v-layout row wrap>
                      <v-flex xs12><v-select :items="typeItems" v-model="typeSelect" label="节点类型" >
                        <template slot="selection" slot-scope="data">
                          {{ data.item.text }}
                          <v-spacer></v-spacer>
                          <v-icon>{{ data.item.icon }}</v-icon>
                        </template>
                        <template slot="item" slot-scope="data">
                          {{ data.item.text }}
                          <v-spacer></v-spacer>
                          <v-icon>{{ data.item.icon }}</v-icon>
                        </template>
                      </v-select>
                    </v-flex>
                    </v-layout>
                  </v-container>
                </v-flex>
              </v-layout>
            </v-container>
            <template v-if="typeSelect=='SSR'">
              <v-container fluid>
                <v-form v-model="ssr" ref="ssr">
                  <v-layout row wrap>
                    <v-flex xs6>
                      <v-text-field v-model="nodeName" :rules="noEmpty" :counter="25" label="节点名称" clearable required></v-text-field>
                    </v-flex>
                    <v-flex xs6>
                      <v-text-field v-model="subtitle"  :counter="64" label="附加信息" clearable></v-text-field>
                    </v-flex>
                    <v-flex xs4>
                      <v-text-field v-model="ssrAddr" :rules="ipRules" label="节点IP" required></v-text-field>
                    </v-flex>
                    <v-flex xs2>
                      <v-text-field v-model="ssrPort" :rules="portRules" label="端口" required></v-text-field>
                    </v-flex>
                    <v-flex xs6>
                      <v-text-field v-model="ssrPsw" :rules="noEmpty" label="节点密码" clearable required></v-text-field>
                    </v-flex>
                    <v-flex xs6>
                      <v-select :items="ssrMethodItems" v-model="ssrMethod" label="加密方法" ></v-select>
                    </v-flex>
                    <v-flex xs6>
                      <v-select :items="ssrProtocolItems" v-model="ssrProtocol" label="协议类型" ></v-select>
                    </v-flex>
                    <v-flex xs6>
                      <v-text-field v-model="ssrProtocolParam" label="协议参数" clearable></v-text-field>
                    </v-flex>
                    <v-flex xs6>
                      <v-select :items="ssrObfsItems" v-model="ssrObfs" label="混淆类型" ></v-select>
                    </v-flex>
                    <v-flex xs6>
                      <v-text-field v-model="ssrObfsParam" label="混淆参数" clearable></v-text-field>
                    </v-flex>
                    <v-flex xs6>

                        <v-radio-group v-model="ssrStatu" row placeholder="状态">
                          <v-radio label="↓" value=-1 ></v-radio>
                          <v-radio label="?" value=0></v-radio>
                          <v-radio label="↑" value=1></v-radio>
                        </v-radio-group>
  
                    </v-flex>
                  </v-layout>
                </v-form>
              </v-container>
            </template>
            <template v-else-if="typeSelect=='V2ray'">
              <v-container fluid>
                <v-form v-model="v2ray" ref="v2ray">
                  <v-layout row wrap>
                    <v-flex xs6>
                      <v-text-field v-model="nodeName" :rules="noEmpty" :counter="25" label="节点名称" clearable required></v-text-field>
                    </v-flex>
                    <v-flex xs6>
                      <v-select :items="v2ProtocolItems" v-model="v2Protocol" label="传入协议" ></v-select>
                    </v-flex>
                    <template v-if="v2Protocol=='Shadowsocks'">
                      <v-flex xs6>
                        <v-text-field v-model="v2Addr" :rules="v2AddrRules" label="节点地址" required></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                        <v-text-field v-model="v2Email" :rules="emailRules" label="邮箱地址" clearable required></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                        <v-select :items="v2MethodItmes" v-model="v2Method" label="加密方式" ></v-select>
                      </v-flex>
                      <v-flex xs6>
                        <v-text-field v-model="v2Psw" label="密码" :counter="25"></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                        <v-select v-model="v2Network" label="服务器网络协议" :items="v2NetworkItems" ></v-select>
                      </v-flex>
                    </template>
                    <template v-else-if="v2Protocol=='SOCKS'">
                      <v-flex xs6>
                        <v-text-field v-model="v2Addr" :rules="v2AddrRules" label="节点地址" required></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                         <v-text-field v-model="v2InboundPort" label="端口" :rules="portRules" required></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                        <v-text-field v-model="v2User" label="用户名" :rules="noEmpty" required></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                        <v-text-field v-model="v2Psw" label="密码" :rules="noEmpty" required></v-text-field>
                      </v-flex>
                    </template>
                    <template v-else-if="v2Protocol=='VMess'">
                      <v-flex xs6>
                        <v-text-field v-model="v2InboundPort" label="传入端口" :rules="portRules" required></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                        <v-text-field v-model="v2Addr" :rules="v2AddrRules" label="节点地址" required></v-text-field>
                      </v-flex>
                      <v-flex xs10>
                        <v-text-field v-model="v2UUID" label="用户UUID" :rules="uuidRules" required></v-text-field>
                      </v-flex>
                      <v-flex xs2>
                        <v-text-field v-model="v2AlterId" label="额外ID" :rules="alterIdRules" required></v-text-field>
                      </v-flex>
                    </template>
                    
                    <v-flex xs6>
                      <v-select :items="v2TransportItems" v-model="v2Transport" label="传输配置" ></v-select>
                    </v-flex>
                    <template v-if="v2Transport=='TCP'">
                      <v-flex xs6>
                        <v-select :items="v2TCPHeaderPretend" v-model="v2TCPHeader" label="头部伪装" ></v-select>
                      </v-flex>
                    </template>
                    <template v-else-if="v2Transport=='mKCP'">
                      <v-flex xs6>
                        <v-select :items="v2KCPHeaderPretend" v-model="v2KCPHeader" label="头部伪装" ></v-select>
                      </v-flex>
                    </template>
                    <template v-else-if="v2Transport=='webSocket'">
                      <v-flex xs6>
                        <v-text-field v-model="v2WebSocketPath" label="HTTP协议路径"></v-text-field>
                      </v-flex>
                    </template>
                    <template v-else-if="v2Transport=='HTTP/2'">
                      <v-flex xs6>
                        <v-text-field v-model="v2HTTP2Host" label="通信域名"></v-text-field>
                      </v-flex>
                      <v-flex xs6>
                        <v-text-field v-model="v2HTTP2Path" label="HTTP协议路径"></v-text-field>
                      </v-flex>
                    </template>
                    <v-flex xs6>
                      <v-switch :label="`使用TLS: ${tlsEnable}`" v-model="tlsEnable" ></v-switch>
                    </v-flex>
                  </v-layout>
                </v-form>
              </v-container>
            </template>
            <template v-else-if="typeSelect=='Bak1'"></template>
            <template v-else-if="typeSelect=='Bak2'"></template>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" flat @click.stop="dialog=false">取消</v-btn>
            <v-btn color="primary" flat @click.native="addNode()">添加</v-btn>
          </v-card-actions>
        </v-card>
    </v-dialog>
     <v-snackbar :color="snackbarColor" v-model="snackbar">{{ alertText }}</v-snackbar>
  </v-app>
</template>
<script>
import * as types from './store/types'
import Aplayer from 'vue-aplayer'
export default {
  data: () => ({
    isRouterAlive: true,
    loged: false,
    dialog: false,
    drawer: null,
    snackbar: false,
    alertText: '',
    snackbarColor: 'success',
    typeSelect: 'SSR',
    defaultMusic: {
      title: 'secret base~君がくれたもの~',
      artist: 'Silent Siren',
      src: 'https://moeplayer.b0.upaiyun.com/aplayer/secretbase.mp3',
      pic: 'https://moeplayer.b0.upaiyun.com/aplayer/secretbase.jpg'
    },
    musicList : [],
    noEmpty: [
      v => !!v || "不能为空"
    ],
    ipRules: [
      v => !!v || "不能为空",
      v => /^((2[0-4][0-9]|25[0-5]|[01]?[0-9][0-9]?).){3}(2[0-4][0-9]|25[0-5]|[01]?[0-9][0-9]?)$/.test(v) || "格式不正确"
    ],
    portRules: [
      v => !!v || "不能为空",
      v => v>0 && v<65535 || "端口号不正确"
    ],
    v2AddrRules: [
      v => !!v || "不能为空",
      v => /^((2[0-4][0-9]|25[0-5]|[01]?[0-9][0-9]?).){3}(2[0-4][0-9]|25[0-5]|[01]?[0-9][0-9]?)$/.test(v) || /^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$/.test(v) || "格式不正确"
    ],
    uuidRules: [
      v => !!v || "不能为空",
      v => /^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$/.test(v) || "格式不正确"
    ],
    alterIdRules: [
      v => !!v || "不能为空",
      v => v>=0 && v<=65535 || "额外Id不正确"
    ],
    emailRules: [
      v => !!v || "不能为空",
      v => /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$/.test(v) || "格式不正确"
    ],
    user: {
      head: '24935690',
      name: 'Delitto'
    },
    menus : null,
    typeItems: [
      { text: 'SSR', value: 'SSR', icon: 'send' },
      { text: 'V2Ray', value: 'V2ray', icon: 'send' },
      { text: 'Bak1', value: 'Bak1', icon: 'send' },
      { text: 'Bak2', value: 'Bak2', icon: 'send' }
    ],
    ssr: null,
    nodeName: null,
    subtitle: '',
    ssrAddr: null,
    ssrPort: null,
    ssrPsw: null,
    ssrMethod: 'none',
    ssrProtocol: 'origin',
    ssrObfs: 'plain',
    ssrMethodItems: [
      { text: "none", value: "none"},
      { text: "table", value: "table"},
      { text: "rc4", value: "rc4"},
      { text: "rc4-md5", value: "rc4-md5"},
      { text: "rc4-md5-6", value: "rc4-md5-6"},
      { text: "aes-128-cfb", value: "aes-128-cfb"},
      { text: "aes-192-cfb", value: "aes-192-cfb"},
      { text: "aes-256-cfb", value: "aes-256-cfb"},
      { text: "aes-128-ctr", value: "aes-128-ctr"},
      { text: "aes-192-ctr", value: "aes-192-ctr"},
      { text: "aes-256-ctr", value: "aes-256-ctr"},
      { text: "chacha20", value: "chacha20"},
      { text: "chacha20-ietf", value: "chacha20-ietf"}
    ],
    ssrProtocolItems: [
      { text: "origin", value: "origin"},
      { text: "auth_sha1", value: "auth_sha1"},
      { text: "auth_sha1_v2", value: "auth_sha1_v2"},
      { text: "auth_sha1_v4", value: "auth_sha1_v4"},
      { text: "auth_aes128_sha1", value: "auth_aes128_sha1"},
      { text: "auth_aes128_md5", value: "auth_aes128_md5"},
      { text: "auth_chain_a", value: "auth_chain_a"}
    ],
    ssrProtocolParam: '',
    ssrObfsItems: [
      { text: "plain", value: "plain"},
      { text: "http_simple", value: "http_simple"},
      { text: "http_post", value: "http_post"},
      { text: "tls_simple", value: "tls_simple"},
      { text: "tls1.2_ticket_auth", value: "tls1.2_ticket_auth"}
    ],
    ssrObfsParam: '',
    ssrStatu: -1,
    v2ray: null,
    v2InboundPort: null,
    v2Addr: null,
    v2UUID: null,
    v2AlterId: null,
    v2Email: null,
    v2User: null,
    v2Psw: null,
    v2Transport: 'TCP',
    v2TransportItems: [
      { text: "TCP", value: "TCP"},
      { text: "mKCP", value: "mKCP"},
      { text: "webSocket", value: "webSocket"},
      { text: "HTTP/2", value: "HTTP/2"}
    ],
    v2TCPHeader: 'none',
    v2TCPHeaderPretend: [
      { text: "不伪装", value: "none"},
      { text: "HTTP", value: "http"}
    ],
    v2Protocol: 'VMess',
    v2ProtocolItems: [
      { text: "HTTP", value: "HTTP"},
      { text: "Shadowsocks", value: "Shadowsocks"},
      { text: "SOCKS", value: "SOCKS"},
      { text: "VMess", value: "VMess"}
    ],
    tlsEnable: false,
    v2KCPHeader: 'none',
    v2KCPHeaderPretend: [
      { text: "不伪装", value: "none"},
      { text: "视频通话", value: "srtp"},
      { text: "BT下载", value: "utp"},
      { text: "微信视频", value: "wechat-video"}
    ],
    v2Method: "aes-256-cfb",
    v2MethodItmes: [
      { text: "aes-256-cfb", value: "aes-256-cfb"},
      { text: "aes-128-cfb", value: "aes-128-cfb"},
      { text: "chacha20", value: "chacha20"},
      { text: "chacha20-ietf", value: "chacha20-ietf"},
      { text: "aes-256-gcm", value: "aes-256-gcm"},
      { text: "aes-128-gcm", value: "aes-128-gcm"},
      { text: "chacha20-poly1305", value: "chacha20-poly1305"}
    ],
    v2Network: 'tcp',
    v2NetworkItems: [
      { text: "TCP", value: "tcp"},
      { text: "UDP", value: "udp"},
      { text: "TCP,UDP", value: "tcp,udp"}
    ],
    v2WebSocketPath: null,
    v2HTTP2Host: null,
    v2HTTP2Path: null

  }),
  methods: {
    getMenu() {
      this.axios.get('/api/menu').then((response) => {
        if(response.status == 200) {
            this.menus = response.data.data
            if(!response.data.statu){
              this.logout()
            }
        }else{
          console.log("Menu Error")
        }
      })
      this.changeStatu()
    },
    addNode() {
      if(this.$refs.ssr){
        if(this.$refs.ssr.validate()){
          this.axios.post('/api/nodes', {
            'type': 'saveSSR',
            'node': {
              'nodeName': this.nodeName,
              'subtitle': this.subtitle,
              'addr': this.ssrAddr,
              'port': this.ssrPort,
              'psw': this.ssrPsw,
              'method': this.ssrMethod,
              'protocol': this.ssrProtocol,
              'obfs': this.ssrObfs,
              'protocolParam': this.ssrProtocolParam,
              'obfsParam': this.ssrObfsParam,
              'statu': this.ssrStatu
            }
          }).then(() => {
            this.alertText = '添加成功'
            this.snackbarColor = 'success'
            this.snackbar = true
            this.dialog = false
            this.reload()
          }).catch((err) => {
            console.log(err)
            this.alertText = '网络异常'
            this.snackbarColor = 'error'
            this.snackbar = true
            this.dialog = false
          })

        }
      }else if(this.$refs.v2ray){
        if(this.$refs.v2ray.validate()){
          this.snackbarColor = 'success'
          this.alertText = '添加成功'
          this.snackbar = true
          this.dialog = false
        }
      }
    },
    logout() {
      this.$store.commit(types.LOGOUT)
      this.$router.push({
        path: '/auth'
      })
    },
    changeStatu() {
      this.loged = this.$store.state.loged
    },
    reload () {
      this.isRouterAlive = false
      this.$nextTick(() => (this.isRouterAlive = true))
    },
  },
  created() {
    this.getMenu()
    this.loged = this.$store.state.loged
  },
  watch: {
    '$route': 'getMenu'
  },
  components: {
    'aplayer': Aplayer
  },
  name: 'App'
}

</script>
