from flamingo.core.views import View


class Post(View):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class PostList(View):
    def get(self):
        return self.response("hello Post")

    def post(self):
        pass
