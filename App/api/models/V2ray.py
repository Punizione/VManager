from App import db

class V2ray(db.Model):
	__tablename__ = 'v2ray'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	nodename = db.Column(db.String(32), nullable=False)
	subtitle = db.Column(db.String(64), nullable=True)
	addr = db.Column(db.String(64), nullable=False)
	port = db.Column(db.Integer, default=443, nullable=False)

	protocol = db.Column(db.String(32), default='VMess', nullable=False)
	transport = db.Column(db.String(16), default='TCP', nullable=False)
	tlsenable = db.Column(db.Boolean, default=False, nullable=False)

	#Protocol
	#Vmess
	uuid = db.Column(db.String(64), default='', nullable=True)
	alterid = db.Column(db.Integer, default=64, nullable=True)
	
	#Shadowsocks
	email = db.Column(db.String(64), default='', nullable=True)
	method = db.Column(db.String(32), default='', nullable=True)
	psw = db.Column(db.String(32), default='', nullable=True)
	network = db.Column(db.String(16), default='TCP', nullable=True)

	#SOCKS
	user = db.Column(db.String(32), default='', nullable=True)

	#HTTP
	#nothing

	#Transport
	#TCP
	tcpheader = db.Column(db.String(16), default='none', nullable=True)
	#mKCP
	kcpheader = db.Column(db.String(16), default='none', nullable=True)
	#WebSocket
	websocketpath = db.Column(db.String(128), default='', nullable=True)
	#HTTP/2
	http2host = db.Column(db.String(64), default='', nullable=True)
	http2path = db.Column(db.String(128), default='', nullable=True)

	statu = db.Column(db.Integer, default=0, nullable=False)


	def __init__(
		self,
		id=None,
		nodename=None,
		subtitle=None,
		addr=None,
		port=None,
		protocol=None,
		transport=None,
		tlsenable=False,
		uuid=None,
		alterid=None,
		email=None,
		method=None,
		psw=None,
		network=None,
		user=None,
		tcpheader=None,
		kcpheader=None,
		websocketpath=None,
		http2host=None,
		http2path=None,
		statu=None):
		self.id = id
		self.nodename = nodename
		self.subtitle = subtitle
		self.addr = addr
		self.port = port
		self.protocol = protocol
		self.transport = transport
		self.tlsenable = tlsenable
		self.uuid = uuid
		self.alterid = alterid
		self.email = email
		self.method = method
		self.psw = psw
		self.network = network
		self.user = user
		self.tcpheader = tcpheader
		self.kcpheader = kcpheader
		self.websocketpath = websocketpath
		self.http2host = http2host
		self.http2path = http2path
		self.statu = statu

	@staticmethod
	def queryWithUser():
		v2_list = V2ray.query.all()
		li = []
		ret = {}
		if v2_list and len(v2_list) > 0:
			for node in v2_list:
				li.append({
					"id": node.id,
					"nodeName": node.nodename,
					"subTitle": node.subtitle,
					"addr": node.addr,
					"port": node.port,
					"protocol": node.protocol,
					"transport": node.transport,
					"tlsEnable": node.tlsenable,
					"UUID": node.uuid,
					"alterId": node.alterid,
					"email": node.email,
					"method": node.method,
					"psw": node.psw,
					"network": node.network,
					"user": node.user,
					"TCPHeader": node.tcpheader,
					"KCPHeader": node.kcpheader,
					"webSocketPath": node.websocketpath,
					"http2Host": node.http2host,
					"http2Path": node.http2path,
					"statu": node.statu,
					't': False,
					'ty': 'V2Ray'
				})
			ret["empty"] = False
			ret["nodes"] = li
		else:
			ret["empty"] = True
		return ret

	@staticmethod
	def queryWithVisitor():
		v2_list = V2ray.query.all()
		li = []
		ret = {}
		if v2_list and len(v2_list) > 0:
			for node in v2_list:
				li.append({
					"id": node.id,
					"nodeName": node.nodename,
					"subtitle": node.subtitle,
					"statu": node.statu,
					't': True,
					'ty': 'V2Ray'
				})
			ret["empty"] = False
			ret["nodes"] = li
		else:
			ret["empty"] = True
		return ret


	@staticmethod
	def edit(
		id,
		nodename=None,
		subtitle=None,
		addr=None,
		port=None,
		protocol=None,
		transport=None,
		tlsenable=False,
		uuid=None,
		alterid=None,
		email=None,
		method=None,
		psw=None,
		network=None,
		user=None,
		tcpheader=None,
		kcpheader=None,
		websocketpath=None,
		http2host=None,
		http2path=None,
		statu=None):
		n = V2ray.query.filter(V2ray.id == id).first()
		n.nodename = nodename
		n.subtitle = subtitle
		n.addr = addr
		n.port = port
		n.protocol = protocol
		n.transport = transport
		n.tlsenable = tlsenable
		n.uuid = uuid
		n.alterid = alterid
		n.email = email
		n.method = method
		n.psw = psw
		n.network = network
		n.user = user
		n.tcpheader = tcpheader
		n.kcpheader = kcpheader
		n.websocketpath = websocketpath
		n.http2path = http2path
		n.http2host = http2host
		n.statu = statu
		db.session.commit()

	@staticmethod
	def dele(id):
		n = V2ray.query.filter(V2ray.id == id).first()
		db.session.delete(n)
		db.session.commit()

	def save(self):
		db.session.add(self)
		db.session.commit()
