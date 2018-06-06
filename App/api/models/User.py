from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from App import db
from passlib.handlers.django import django_pbkdf2_sha256
import uuid as UUID
import base64

class User(db.Model):
	__tablename__ = 'users'
	uuid = db.Column(db.String(22), primary_key=True)
	username = db.Column(db.String(64), unique=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)
	active = db.Column(db.Boolean(), default=True, nullable=False)

	def __init__(self, username, password, active=True):
		self.uuid = base64.urlsafe_b64encode(UUID.uuid4().bytes)[:-2].decode('utf-8')
		self.username = username
		self.password = django_pbkdf2_sha256.encrypt(password).encode('utf-8')
		self.active = active




	@staticmethod
	def authenticate(username, password):
		user = User.query.filter(User.username == username).first()
		if user and django_pbkdf2_sha256.verify(password, user.password):
			return user
		else:
			return None

	@staticmethod
	def changePassword(username, oldpassword, newpassword):
		if username == 'visitor':
			return {'retCode': -2}
		else:
			user = User.query.filter(User.username == username).first()
			if user and django_pbkdf2_sha256.verify(oldpassword, user.password):
				user.password = django_pbkdf2_sha256.encrypt(newpassword).encode('utf-8')
				db.session.commit()
				return {"retCode": 0}
			else:
				return {"retCode": -1}