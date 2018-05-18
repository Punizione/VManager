""" API Backend - Base Resource Models """

from flask_restful import Resource, abort

from App.api import api_rest
from App.api.security import require_auth, require_auth_nodes, require_auth_loged

class BaseResource(Resource):

    def get(self, *args, **kwargs):
        abort(405)

    def post(self, *args, **kwargs):
        abort(405)

    def put(self, *args, **kwargs):
        abort(405)

    def patch(self, *args, **kwargs):
        abort(405)

    def delete(self, *args, **kwargs):
        abort(405)

class SecureResource(BaseResource):
    method_decorators = [require_auth]

class HalfProtectResource(BaseResource):
    method_decorators = [require_auth_nodes]

class CheckAuthorizationResource(BaseResource):
    method_decorators = [require_auth_loged]

def rest_resource(resource_cls):
    """ Decorator for adding resources to Api App """
    api_rest.add_resource(resource_cls, *resource_cls.endpoints)
