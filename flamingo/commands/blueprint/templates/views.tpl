from flamingo.core.views import View


class {{OBJECT}}(View):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class {{OBJECT}}List(View):
    def get(self):
        return self.response("hello {{OBJECT}}")

    def post(self):
        pass
