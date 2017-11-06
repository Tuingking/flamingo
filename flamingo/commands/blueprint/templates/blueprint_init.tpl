from flask import Blueprint
from flask_restful import Api

bp = Blueprint('{{BP_NAME}}', __name__)
api = Api(bp)
