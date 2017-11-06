import random
import string

from flask_script import Command, Option


class Keygen(Command):
    """Generate random key of digit and number (default length:32)
    """

    def get_options(self):
        return [
            Option('-l', '--length', dest='length', default=32)
        ]

    def run(self, length=32):
        secret_key = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for x in range(length))

        return secret_key
