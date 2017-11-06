import os
from shutil import copyfile, move

from flask_script import Command, Option


CURRENT_PATH = os.path.dirname(__file__)


class MakeBlueprint(Command):
    """Create blueprint"""

    def get_options(self):
        return [
            Option('-n', '--name', dest='name', default=None)
        ]

    def run(self, name=None):
        if not name:
            return "Please enter blueprint's name"
        else:
            name = name.lower()

        bp_dir_path = create_blueprint_dir(name)
        create_init_file(bp_dir_path, bp_name=name)       # __init__.py


def create_blueprint_dir(dir_name):
    api_dir = os.path.join(CURRENT_PATH, '..', '..', '..', 'app', '')
    dir_name = dir_name.lower()

    full_path = api_dir + dir_name

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return full_path


def create_init_file(path, bp_name):
    template_path = os.path.join(
        CURRENT_PATH, 'templates', 'blueprint_init.tpl')
    object_path = path + "/__init__.py"

    # copy to folder api
    copyfile(template_path, object_path)

    # replace string
    replace_string(source=path + '/__init__.py',
                   dest=path + '/__init__temp.py',
                   tpl_string='{{BP_NAME}}',
                   new_string=bp_name)


def replace_string(source, dest, tpl_string, new_string):
    with open(source, "rt") as fin:
        with open(dest, "wt") as fout:
            for line in fin:
                fout.write(
                    line.replace(tpl_string, new_string))

    # rename
    move(dest, source)

    return True
