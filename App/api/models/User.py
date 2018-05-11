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

	def __init__(self, username, password):
		self.uuid = base64.urlsafe_b64encode(UUID.uuid4().bytes)[:-2].decode('utf-8')
		self.username = username.encode('utf-8')
		self.password = django_pbkdf2_sha256.encrypt(password).encode('utf-8')
		self.active = True




	@staticmethod
	def authenticate(username, password):
		user = User.query.filter(User.username == username).one()
		if user and django_pbkdf2_sha256.verify(password, user.password):
			return user
		else:
			return None