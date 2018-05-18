""" Security Related things """
from functools import wraps
from flask_restful import abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from App.api.models.User import User
from App import app
import jwt
import datetime
import time
from flask import request, g
def require_auth(func):
    """ Secure method decorator """
    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        if not header:
            abort(401, message='Not Token')
        else:
            _, token = header.split()
            try:
                decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            except jwt.DecodeError:
                abort(400)
            except jwt.ExpiredSignatureError:
                abort(400)
            if not decode['username']:
                abort(401)
            elif time.mktime(datetime.datetime.utcnow().timetuple()) > decode['exp']:
                abort(401)
            else:
                user = User.query.filter_by(username = decode['username']).first()
                if not user:
                    abort(401)
                else:
                    g.user = user
                    return func(*args, **kwargs)
    return wrapper

def require_auth_nodes(func):
    """ Secure method decorator """
    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        if not header:
            abort(401, message='Not Token')
        else:
            _, token = header.split()
            try:
                decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithm="HS256")
            except jwt.DecodeError:
                abort(400)
            except jwt.ExpiredSignatureError:
                abort(401)
            if not decoded['username']:
                abort(401)
            else:
                user = User.query.filter_by(username = decoded['username']).first()
                if not user:
                    g.user = User("visitor", '', False)
                    return func(*args, **kwargs)
                else:
                    g.user = user
                    return func(*args, **kwargs)
    return wrapper


def require_auth_loged(func):
    """ Check Authorization """
    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        if header:
            _, token = header.split()
            try:
                decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithm="HS256")
            except jwt.DecodeError:
                g.user = User('NOLOG', '', False)
                return func(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                print(1)
                g.user = User('NOLOG', '', False)
                return func(*args, **kwargs)
            if not decoded['username']:
                g.user = User('NOLOG', '', False)
            else:
                g.user = User('LOGED', '', False)
        else:
            g.user = User('NOLOG', '', False)
        return func(*args, **kwargs)

    return wrapper

