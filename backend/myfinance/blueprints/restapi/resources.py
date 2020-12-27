from flask import jsonify
from flask_restful import Resource


class TestResource(Resource):
    def get(self):
        return jsonify(oi="td bm?")