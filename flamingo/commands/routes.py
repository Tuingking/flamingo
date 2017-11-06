from urllib.parse import unquote

from flask_script import Command, Option

from app import create_app


class Routes(Command):
    """Generate application url map
    """

    def get_options(self):
        return [
            # Option('-l', '--length', dest='length', default=32)
        ]

    def run(self, length=32):
        myapp = create_app('dev')
        output = []
        for rule in myapp.url_map.iter_rules():
            methods = ','.join(rule.methods)
            line = unquote("{:50s} {:20s} {}".format(
                rule.endpoint, methods, rule))
            output.append(line)

        for line in sorted(output):
            print(line)
