from flamingo.core.views import View


class Hello(View):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class HelloList(View):
    def get(self):
        return self.response("hello Hello")

    def post(self):
        pass
