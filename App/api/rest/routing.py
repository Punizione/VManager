"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request,g
from App.api.rest.base import BaseResource, SecureResource, HalfProtectResource, CheckAuthorizationResource, rest_resource
from App.api.tools.verifyCodeTools import VerifyCode
from App.api.models.User import User
from App.api.models.Ssr import Ssr
from flask_restful import abort
import datetime
import time
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
        return {'name': 'Resource Two', 'data': resource_id }

@rest_resource
class NodeResource(HalfProtectResource):
    """ /api/nodes """
    endpoints = ['/nodes']

    def get(self):
        if g.user.username == b'visitor':
            if request.args.get('t') == 'SSR':
                return Ssr.queryWithVisitor()
        else:
            if request.args.get('t') == 'SSR':
                return Ssr.queryWithUser()

    def post(self):
        if g.user.username != b'visitor':
            json_payload = request.json
            typ = json_payload['type']
            n = json_payload['node']
            if typ == 'editSSR':
                Ssr.edit(
                    n['id'],
                    n['nodeName'],
                    n['subtitle'],
                    n['addr'],
                    n['port'],
                    n['psw'],
                    n['method'],
                    n['protocol'],
                    n['protocolParam'],
                    n['obfs'],
                    n['obfsParam'],
                    n['statu']
                    )
            elif typ == 'saveSSR':
                node = Ssr(
                    nodename=n['nodeName'],
                    subtitle=n['subtitle'],
                    addr=n['addr'],
                    port=n['port'],
                    psw=n['psw'],
                    method=n['method'],
                    protocol=n['protocol'],
                    protocolparam=n['protocolParam'],
                    obfs=n['obfs'],
                    obfsparam=n['obfsParam'],
                    statu=n['statu']
                )
                node.save()
            elif typ == 'deleteSSR':
                Ssr.dele(id=n['id'])





@rest_resource
class MenuResource(CheckAuthorizationResource):
    """ /api/menu """
    endpoints = ['/menu']
    
    def get(self):
        noLogin = {'statu': False, 'data':[{'title': 'LOGIN','items': [{'icon': 'fingerprint', 'text': '登录', 'url': '/auth'}]}]}

        loged = {'statu': True,
                'data': [{'title': 'NODES',  'items': [
                    {'icon': 'list', 'text': '节点列表', 'url': '/list'},
                    {'icon': 'trending_up', 'text': '节点测速', 'url': '/speedtest'},
                    {'icon': 'help', 'text': '使用教程', 'url': '/tips'}
                    ]},{'title': 'USER','items': [
                    {'icon': 'rss_feed', 'text': '用户订阅', 'url': '/rss'},
                    {'icon': 'settings', 'text': '用户设置', 'url': '/setting'},
                    {'icon': 'cloud_download', 'text': '资源下载', 'url': '/download'}
                ]}
            ]}
        if g.user and g.user.username == b'LOGED':
            return loged
        else:
            return noLogin

@rest_resource
class VerifyCodeResource(BaseResource):
    """ /api/code , /api/verify"""
    endpoints = ['/code', '/verify']
    
    def get(self):
        url, code = VerifyCode.genPicture()
        return { 'url': url, 'h': code}


    def post(self):
        json_payload = request.json
        code = json_payload['code']
        pictureHash = json_payload['h']
        if VerifyCode.verify(code, pictureHash):
            return { 'retCode': 1 }
        else:
            return { 'retCode': 0 }


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
            exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['SECURITY_TOKEN_USER_HOUR'])
            encode = jwt.encode({
                'username': username,
                'exp': exp
            }, app.config['SECRET_KEY'], algorithm="HS256")
            return { 'retCode': 1, "token": encode.decode('utf-8') }
        else:
            return { 'retCode': 0 }

@rest_resource
class VisitorLoginResource(BaseResource):
    """ /api/auth/temp """
    endpoints = ['/auth/temp']
    def post(self):
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['SECURITY_TOKEN_VISITOR_HOUR'])
        encode = jwt.encode({
            'username': 'visitor',
            'exp': exp
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return { 'retCode': 1, "token": encode.decode('utf-8') }


@rest_resource
class RegisterResource(BaseResource):
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

            return { 'username': username, 'token': encode.decode('utf-8')}

