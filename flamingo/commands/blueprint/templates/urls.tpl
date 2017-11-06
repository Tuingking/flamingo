from .views import {{OBJECT_CAPITALIZE}}, {{OBJECT_CAPITALIZE}}List
from .. import api

api.add_resource({{OBJECT_CAPITALIZE}}, '/{{OBJECT_LOWER}}s/<int:id>')
api.add_resource({{OBJECT_CAPITALIZE}}List, '/{{OBJECT_LOWER}}s')
