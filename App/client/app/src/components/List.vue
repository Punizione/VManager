<template>
  <v-parallax :src="`http://p0s30qphu.bkt.clouddn.com/18-1-8/13633991.jpg`" height="1000" >
    <v-content class="px-0 py-0">
      <v-container fluid>
        <v-layout column>
          <v-flex xs12 sm6>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>节点列表</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-menu left bottom>
                <v-btn slot="activator" icon>
                  <v-icon>view_carousel</v-icon>
                </v-btn>
                 <v-list>
                  <v-list-tile v-for="item in nodeType" :key='item' @click="fetchData(item)">
                    <v-list-tile-title>{{ item }}</v-list-tile-title>
                  </v-list-tile>
                </v-list>
              </v-menu>
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
            <template v-else-if="empty" class="empty"></template>
            <template v-else>
              <v-card>
                <v-container fluid grid-list-md>
                  <v-layout row wrap>
                    <v-flex xs12 sm12>
                      <v-list two-line>
                        <template v-for="(item, index) in nodes">
                          <v-list-tile avatar ripple @click.native.stop="openDialog(item)" :key="item.nodename">
                            <v-list-tile-content>
                              <v-list-tile-title>{{ item.ty }}-{{ item.nodeName }}</v-list-tile-title>
                              <v-list-tile-sub-title>{{ item.subTitle }}</v-list-tile-sub-title>
                            </v-list-tile-content>
                            <v-list-tile-action>
                              <v-icon color="red" v-if="item.statu==-1">error</v-icon>
                              <v-icon color="yellow darken-2" v-else-if="item.statu==0">report_problem</v-icon>
                              <v-icon color="green" v-else>cloud_done</v-icon>
                            </v-list-tile-action>
                              <v-btn v-if="!item.t" color="primary" @click.stop="showEditModal(item)">编辑</v-btn>
                              <v-btn v-if="!item.t" color="primary"
                              @click.stop="dele(item)">删除</v-btn>
                          </v-list-tile>
                          <v-divider v-if="index + 1 < nodes.length" :key="index"></v-divider>
                        </template>
                      </v-list>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card>
              <template id="modal">
                <v-dialog v-model="dialog" max-width="300">
                  <v-card>
                    <v-card-media v-if="node.t" :src="`http://p0s30qphu.bkt.clouddn.com/17-12-11//${ node.pic }.jpg`" height="200px" contain>
                    </v-card-media>
                    <v-card-media v-if="!node.t" :src="this.currentQr" height="200px" contain>
                    </v-card-media>
                    <v-card-title class="headline">{{ node.nodeName }}</v-card-title>
                    <v-card-text>{{ node.subTitle }}</v-card-text>
                  </v-card>
                </v-dialog>
              </template>
            </template>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-dialog v-model="editDialog" max-width="500px">
        <v-card>
          <v-card-title primary-title>
            编辑节点
          </v-card-title>
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
                          <v-radio label="↓" value='-1'></v-radio>
                          <v-radio label="?" value='0'></v-radio>
                          <v-radio label="↑" value='1'></v-radio>
                        </v-radio-group>
  
                    </v-flex>
                  </v-layout>
                </v-form>
              </v-container>
            </template>
            <template v-else-if="typeSelect=='V2Ray'">
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
                         <v-text-field v-model="v2Port" label="端口" :rules="portRules" required></v-text-field>
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
                        <v-text-field v-model="v2Port" label="传入端口" :rules="portRules" required></v-text-field>
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
            <v-btn color="primary" flat @click.native="editNode()">保存</v-btn>
          </v-card-actions>
        </v-card>
    </v-dialog>
     <v-snackbar :color="snackbarColor" v-model="snackbar">{{ alertText }}</v-snackbar>
  </v-parallax>
</template>
<script>
import QRCode from 'qrcode'
var base64 = require('node-base64-urlsafe');
export default {
  data() {
    return {
      
      snackbar: false,
      snackbarColor: 'error',
      alertText: "",
      editDialog: false,
      dialog: false,
      loaded: false,
      nodes: [],
      node: {
        id: null,
        nodename: null,
        subtitle: null,
        statu: null,
        pic: null
      },
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
      currentQr: '',
      empty: false,
      nodeType: [
        'SSR',
        'V2Ray',
        'Bak1',
        'Bak2'
      ],
      mainparallax: null,
      typeSelect: null,
      ssr: null,
      nodeName: null,
      subtitle: '',
      ty: null,
      ssrId: null,
      ssrAddr: null,
      ssrPort: null,
      ssrPsw: null,
      ssrMethod: 'none',
      ssrProtocol: 'origin',
      ssrProtocolParam: '',
      ssrObfs: 'plain',
      ssrObfsParam: '',
      ssrStatu: -1,
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
      ssrObfsItems: [
        { text: "plain", value: "plain"},
        { text: "http_simple", value: "http_simple"},
        { text: "http_post", value: "http_post"},
        { text: "tls_simple", value: "tls_simple"},
        { text: "tls1.2_ticket_auth", value: "tls1.2_ticket_auth"}
      ],
      v2ray: null,
      v2Id: null,
      v2Port: null,
      v2Addr: null,
      v2UUID: null,
      v2AlterId: null,
      v2Email: null,
      v2User: null,
      v2Psw: null,
      v2Transport: 'TCP',
      v2TCPHeader: 'none',
      v2Protocol: 'VMess',
      tlsEnable: false,
      v2KCPHeader: 'none',
      v2Method: "aes-256-cfb",
      v2Network: 'tcp',
      v2WebSocketPath: null,
      v2HTTP2Host: null,
      v2HTTP2Path: null,
      v2TransportItems: [
        { text: "TCP", value: "TCP"},
        { text: "mKCP", value: "mKCP"},
        { text: "webSocket", value: "webSocket"},
        { text: "HTTP/2", value: "HTTP/2"}
      ],
      v2TCPHeaderPretend: [
        { text: "不伪装", value: "none"},
        { text: "HTTP", value: "http"}
      ],
      v2ProtocolItems: [
        { text: "HTTP", value: "HTTP"},
        { text: "Shadowsocks", value: "Shadowsocks"},
        { text: "SOCKS", value: "SOCKS"},
        { text: "VMess", value: "VMess"}
      ],
      v2KCPHeaderPretend: [
        { text: "不伪装", value: "none"},
        { text: "视频通话", value: "srtp"},
        { text: "BT下载", value: "utp"},
        { text: "微信视频", value: "wechat-video"}
      ],
      v2MethodItmes: [
        { text: "aes-256-cfb", value: "aes-256-cfb"},
        { text: "aes-128-cfb", value: "aes-128-cfb"},
        { text: "chacha20", value: "chacha20"},
        { text: "chacha20-ietf", value: "chacha20-ietf"},
        { text: "aes-256-gcm", value: "aes-256-gcm"},
        { text: "aes-128-gcm", value: "aes-128-gcm"},
        { text: "chacha20-poly1305", value: "chacha20-poly1305"}
      ],
      v2NetworkItems: [
        { text: "TCP", value: "tcp"},
        { text: "UDP", value: "udp"},
        { text: "TCP,UDP", value: "tcp,udp"}
      ]  
    }
  },
  created() {
    this.fetchData('SSR')
  },
  watch: {
    '$route': "fetchData('SSR')"
  },
  methods: {
    fetchData(nodeType) {
      this.error = this.nodes = null
      this.loaded = false
      this.axios.get('/api/nodes', {
        params: {
          't': nodeType
        }
      }).then((response) => {
        if (response.status == 200) {
            if (response.data.empty) {
              this.empty = true
            } else {
              this.nodes = response.data.nodes
            }
        } else {
          this.error = 'Error'
        }
        this.loaded = true
      }).catch(err => {
        this.loaded = true
      })
    },
    openDialog(item) {
      if(item.ty == 'SSR'){
        this.node = item
        if(!item.t){
          var l = "ssr://"+
          base64.encode(
            item.addr+":"+item.port+":"+item.protocol+":"+item.method+":"+item.obfs+":"+base64.encode(item.psw)+"/?"+"obfsparam="+base64.encode(item.obfsParam)+"&protocolparam="+base64.encode(item.protocolParam)+"&remarks="+base64.encode(item.nodeName+'-'+item.subtitle)+"&group="+base64.encode("Delitto"))
          QRCode.toDataURL(l).then(url => {
              this.currentQr = url
            })
            .catch(err => {
              this.currentQr = 'http://p0s30qphu.bkt.clouddn.com/17-12-11/63455021.jpg'
            })
        }
        this.dialog = true
      }
    },
    showEditModal(item) {
      this.typeSelect = item.ty
      if (this.typeSelect == 'SSR'){
        this.nodeName = item.nodeName
        this.subtitle = item.subtitle
        this.ssrId = item.id
        this.ssrAddr = item.addr
        this.ssrPort = item.port
        this.ssrPsw = item.psw
        this.ssrMethod = item.method
        this.ssrProtocol = item.protocol
        this.ssrObfs = item.obfs
        this.ssrProtocolParam = item.protocolParam
        this.ssrObfsParam = item.obfsParam
        this.ssrStatu = ''+item.statu
        this.editDialog = true
        this.ty = item.ty
      } else if (this.typeSelect == 'V2Ray'){
        this.nodeName = item.nodeName
        this.subtitle = item.subtitle
        this.v2Statu = ''+item.statu
        this.v2Port = item.port
        this.v2Addr = item.addr
        this.v2UUID = item.UUID
        this.v2AlterId = item.alterId
        this.v2Email = item.email
        this.v2User = item.user
        this.v2Psw = item.psw
        this.v2Transport = item.transport
        this.v2TCPHeader = item.TCPHeader
        this.v2KCPHeader = item.KCPHeader
        this.v2Protocol = item.protocol
        this.tlsEnable = item.tlsEnable
        this.v2Method = item.method
        this.v2NetWork = item.network
        this.v2WebSocketPath = item.webSocketPath
        this.v2HTTP2Host = item.http2Host
        this.v2HTTP2Path = item.http2Path
        this.ty = item.ty
        this.editDialog = true

      }
    },
    dele(item) {
      this.axios.post("/api/nodes", {
        type: 'delete'+item.ty,
        node: {
          id: item.id
        }
      }).then(() => {
        this.alertText = '删除成功'
        this.snackbarColor = 'success'
        this.snackbar = true
        this.fetchData(this.typeSelect)
      }).catch(() => {
        this.alertText = '删除失败'
        this.snackbarColor = 'error'
        this.snackbar = true
      })
    },
    editNode() {
      if (this.ty == 'SSR'){
        this.axios.post('/api/nodes', {
          type: 'edit'+this.ty,
          node: {
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
            'statu': this.ssrStatu,
            'id': this.ssrId
          }
        }).then(() => {
          this.alertText = '更新成功'
          this.snackbarColor = 'success'
          this.snackbar = true
          this.editDialog = false
          this.fetchData(this.typeSelect)
        }).catch(() => {
          this.alertText = '更新失败'
          this.snackbarColor = 'error'
          this.snackbar = true
          this.editDialog = false
        })
      } else if(this.ty == 'V2Ray'){
        this.axios.post("/api/nodes", {
          type: 'edit'+this.ty,
          node: {
            'id': this.v2Id,
            'nodeName': this.nodeName,
            'subtitle': this.subtitle,
            'addr': this.v2Addr,
            'port': this.v2Port,
            'protocol': this.v2Protocol,
            'transport': this.v2Transport,
            'tlsEnable': this.tlsEnable,
            'UUID': this.v2UUID,
            'alterId': this.v2AlterId,
            'email': this.v2Email,
            'method': this.v2Method,
            'psw': this.v2Psw,
            'network': this.v2Network,
            'user': this.v2User,
            'TCPHeader': this.v2TCPHeader,
            'KCPHeader': this.v2KCPHeader,
            'webSocketPath': this.v2WebSocketPath,
            'http2Host': this.v2HTTP2Host,
            'http2Path': this.v2HTTP2Path,
            'statu': this.v2Statu
          }
        }).then(() => {
          this.alertText = '更新成功'
          this.snackbarColor = 'success'
          this.snackbar = true
          this.editDialog = false
        }).catch(() => {
          this.alertText = '更新失败'
          this.snackbarColor = 'error'
          this.snackbar = true
          this.editDialog = false
        })
      }
    },


  },
  name: 'List'
}

</script>
