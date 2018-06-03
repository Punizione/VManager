from App import db
import random
from passlib.handlers.django import django_pbkdf2_sha256

class VerifyCode(db.Model):
	__tablename__ = 'verifycode'
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	url = db.Column(db.String(256))
	code = db.Column(db.String(128), nullable=False)


	def __init__(self, url, code):
		self.url = url
		self.code = code.encode('utf-8')


	@classmethod
	def genPicture(cls):
		ran = random.randint(100000000, 999999999)
		count = db.session.query(db.func.count(cls.url)).scalar()
		verifycode = VerifyCode.query.offset(ran%count).first()
		return verifycode.url, django_pbkdf2_sha256.encrypt(verifycode.url).encode('utf-8').decode('utf-8')

	@staticmethod
	def verify(code, pictureHash):
		verifyCode = VerifyCode.query.filter(VerifyCode.code == code).first()
		if verifyCode and django_pbkdf2_sha256.verify(verifyCode.url, pictureHash):
			return True
		else:
			return False
