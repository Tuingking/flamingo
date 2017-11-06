from flask import jsonify
from flask_restful import Resource


class View(Resource):

    def response(self, data, **kwargs):
        status = kwargs.get('status', True)
        message = kwargs.get('message', 'OK')
        data = [] if not data else data

        res = {
            "status": status,
            "message": message,
            "data": data
        }

        return jsonify(res)
