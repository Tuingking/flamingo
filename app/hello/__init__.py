from flask import Blueprint
from flask_restful import Api

bp = Blueprint('hello', __name__)
api = Api(bp)
