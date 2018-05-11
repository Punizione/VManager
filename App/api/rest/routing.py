"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request
from App.api.rest.base import BaseResource, SecureResource, HalfProtectResource, rest_resource
from App.api.models.User import User
from flask_restful import abort
import datetime
import re
from App import db
from App import app
import jwt
@rest_resource
class ResourceOne(BaseResource):
    """ /api/resource/one """
    endpoints = ['/resource/one']

    def get(self):
        time.sleep(1)
        return {'name': 'Resource One', 'data': True}

    def post(self):
        json_payload = request.json
        return {'name': 'Resource Post'}


@rest_resource
class SecureResourceOne(SecureResource):
    """ /api/resource/two """
    endpoints = ['/resource/two/<string:resource_id>']

    def get(self, resource_id):
        time.sleep(1)
        return {'name': 'Resource Two', 'data': resource_id}

@rest_resource
class NodeResource(HalfProtectResource):
    """ /api/nodes """
    endpoints = ['/nodes']

    def get(self):
        if g.user.username == 'visitor':
            return { "empty": True, "mainparallax": "13633991"}
        else:
            return { 
            "empty": False, 
            "nodes": [
                {"id": 1, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 2, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 3, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 4, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 5, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"}
            ],
            "mainparallax": "13633991"
        }
        
        return { "empty": True, "mainparallax": "13633991"}

    def post(self):
        return { 
            "empty": False, 
            "nodes": [
                {"id": 1, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 2, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 3, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 4, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"},
                {"id": 5, "title": "XXX", "transfer": "XXX/XXX", "statu": "0", "pic": "63455021"}
            ],
            "mainparallax": "13633991"
        }

@rest_resource
class UserResource(SecureResource):
    """ /api/user """
    endpoints = ['/user']
    def get(self, username):
        return {"head": "24935690", "name": username}


@rest_resource
class Login(BaseResource):
    """ /api/auth/login """
    endpoints = ['/auth/login']
    def post(self):
        json_payload = request.json
        username = json_payload['username']
        password = json_payload['password']
        user = User.authenticate(username, password)
        if user:
            exp = exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['SECURITY_TOKEN_USER_HOUR'])
            encode = jwt.encode({
                'username': username,
                'exp': exp
            }, app.config['SECRET_KEY'], algorithm="HS256")
            return {'retCode': 1, "token": encode.decode('utf-8') }
        else:
            return { 'retCode': 0 }

@rest_resource
class VisitorLogin(BaseResource):
    """ /api/auth/temp """
    endpoints = ['/auth/temp']
    def post(self):
        exp = exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['SECURITY_TOKEN_VISITOR_HOUR'])
        encode = jwt.encode({
            'username': 'visitor',
            'exp': exp
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return {'retCode': 1, "token": encode.decode('utf-8') }


@rest_resource
class Register(BaseResource):
    """ /api/auth/register """
    endpoints = ['/auth/register']
    def post(self):
        json_payload = request.get_json(force=True)
        print(json_payload)
        username = json_payload['username']
        password = json_payload['password']
        invitecode = json_payload['invitecode']
        if invitecode != 'Delitto':
            abort(400, message="InviteCode Error")
        if not re.match(r'^[A-Za-z0-9]+$', username):
            abort(400, message="Username Error")
        if len(password) < 8:
            abort(400, message="Password Error")
        user = db.session.query(User).filter(User.username == username).first()
        if user:
            abort(401)
        else:
            db.session.add(User(username=username, password=password))
            db.session.commit()
            exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['SECURITY_TOKEN_USER_HOUR'])
            encode = jwt.encode({
                'username': username,
                'exp': exp
            }, app.config['SECRET_KEY'], algorithm="HS256")

            return {'username': username, 'token': encode.decode('utf-8')}

