""" Security Related things """
from functools import wraps
from flask_restful import abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from App.api.models import User
import jwt
import datetime
from flask import request, g
def require_auth(func):
    """ Secure method decorator """
    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        if not header:
            abort(400, message='Not Token')
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
            elif datetima.datetime.utcnow() > decode['exp']:
                abort(401)
            else:
                user = User.query.filter_by(username = decode['username']).one()
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
            abort(400, message='Not Token')
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
            elif datetima.datetime.utcnow() > decode['exp']:
                abort(401)
            else:
                user = User.query.filter_by(username = decode['username']).one()
                if not user:
                    g.user = User("visitor", '', False)
                    return func(*args, **kwargs)
                else:
                    g.user = user
                    return func(*args, **kwargs)
    return wrapper