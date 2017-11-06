from .views import Hello, HelloList
from .. import api

api.add_resource(Hello, '/hellos/<int:id>')
api.add_resource(HelloList, '/hellos')
