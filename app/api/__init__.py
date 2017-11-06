from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)
api = Api(bp)

from .posts import urls as post_url  # noqa: F401
