from .views import Post, PostList
from .. import api

api.add_resource(Post, '/posts/<int:id>')
api.add_resource(PostList, '/posts')
