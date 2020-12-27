from flask import Blueprint
from flask_restful import Api

from .resources import TestResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(TestResource, "/test/")
    app.register_blueprint(bp)