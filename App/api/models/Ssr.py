from App import db



class Ssr(db.Model):
	__tablename__ = 'ssr'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True) 
	nodename = db.Column(db.String(32))
	subtitle = db.Column(db.String(64), nullable=True)
	addr = db.Column(db.String(32), nullable=False)
	port = db.Column(db.Integer, default=443, nullable=False)
	psw = db.Column(db.String(32), nullable=False)
	method = db.Column(db.String(32), default="none", nullable=False)
	protocol = db.Column(db.String(32), default="origin", nullable=False)
	protocolparam = db.Column(db.String(64), nullable=True)
	obfs = db.Column(db.String(32), default="plain", nullable=False)
	obfsparam = db.Column(db.String(64), nullable=True)
	statu = db.Column(db.Integer, default=0, nullable=False)


	def __init__(self, id=None, nodename=None, subtitle=None, addr=None, port=None, psw=None, method=None, protocol=None, protocolparam=None, obfs=None, obfsparam=None, statu=0):
		self.id = id
		self.nodename = nodename
		self.subtitle = subtitle
		self.addr = addr
		self.port = port
		self.psw = psw
		self.method = method
		self.protocol = protocol
		self.protocolparam = protocolparam
		self.obfs = obfs
		self.obfsparam = obfsparam
		self.statu = statu


	@staticmethod
	def queryWithUser():
		ssr_list = Ssr.query.all()
		li = []
		ret = {}
		if ssr_list and len(ssr_list) > 0:
			for node in ssr_list:
				li.append({
					"id": node.id,
					"nodeName": node.nodename,
					"subtitle": node.subtitle,
					"addr": node.addr,
					"port": node.port,
					"psw": node.psw,
					"method": node.method,
					"protocol": node.protocol,
					"protocolParam": node.protocolparam,
					"obfs": node.obfs,
					"obfsParam": node.obfsparam,
					"statu": node.statu,
					't': False,
					'ty': 'SSR'
				})
			ret["empty"] = False
			ret["nodes"] = li
		else:
			ret["empty"] = True
		return ret


	@staticmethod
	def queryWithVisitor():
		ssr_list = Ssr.query.all()
		li = []
		ret = {}
		if ssr_list and len(ssr_list) > 0:
			for node in ssr_list:
				li.append({
					"id": node.id,
					"nodeName": node.nodename,
					"subtitle": node.subtitle,
					"statu": node.statu,
					"pic": "63455021",
					't':True,
					'ty': 'SSR'
				})
			ret["empty"] = False
			ret["nodes"] = li
		else:
			ret["empty"] = True
		return ret
	

	@staticmethod
	def edit(id, nodename, subtitle, addr, port, psw, method, protocol, protocolparam, obfs, obfsparam, statu):
		n = Ssr.query.filter(Ssr.id == id).first()
		n.nodename = nodename
		n.subtitle = subtitle
		n.addr = addr
		n.port = port
		n.psw = psw
		n.method = method
		n.protocol = protocol
		n.protocolparam = protocolparam	
		n.obfs = obfs,
		n.obfsparam = obfsparam
		n.statu = statu
		db.session.commit()

	@staticmethod
	def dele(id):
		n = Ssr.query.filter(Ssr.id == id).first()
		db.session.delete(n)
		db.session.commit()


	def save(self):
		db.session.add(self)
		db.session.commit()

