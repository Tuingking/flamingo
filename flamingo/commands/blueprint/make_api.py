import os
from shutil import copyfile, move

from flask_script import Command, Option


CURRENT_PATH = os.path.dirname(__file__)


class MakeApi(Command):
    """Create blueprint"""

    def get_options(self):
        return [
            Option('-n', '--name', dest='name', default=None)
        ]

    def run(self, name=None):
        if not name:
            return "Please enter api's name,\
            Naming convention: Singular, e.g. post"
        else:
            name = name.capitalize()

        api_dir_path = create_api_dir(name)
        create_empty_file(api_dir_path, name='__init__.py')     # __init__.py
        create_empty_file(api_dir_path, name='models.py')       # models.py
        create_urls(api_dir_path, api_name=name)                # urls.py
        create_views(api_dir_path, api_name=name)               # views.py


def create_api_dir(dir_name):
    api_dir = os.path.join(CURRENT_PATH, '..', '..', '..', 'app', 'api', '')
    dir_name = dir_name.lower()

    # check plural word
    if dir_name[-1] == 's':
        dir_name = dir_name
    else:
        dir_name = dir_name + 's'

    full_path = api_dir + dir_name

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return full_path


def create_empty_file(path, name):
    filename = path + '/' + name
    open(filename, 'a').close()


def create_urls(path, api_name):
    template_path = os.path.join(
        CURRENT_PATH, 'templates', 'urls.tpl')
    object_path = path + "/urls.py"

    # copy to folder api
    copyfile(template_path, object_path)

    # replace string
    replace_string(source=path + '/urls.py',
                   dest=path + '/urls_temp.py',
                   tpl_string='{{OBJECT_LOWER}}',
                   new_string=api_name.lower())

    # replace string
    replace_string(source=path + '/urls.py',
                   dest=path + '/urls_temp.py',
                   tpl_string='{{OBJECT_CAPITALIZE}}',
                   new_string=api_name.capitalize())


def create_views(path, api_name):
    template_path = os.path.join(
        CURRENT_PATH, 'templates', 'views.tpl')
    object_path = path + "/views.py"

    # copy to folder api
    copyfile(template_path, object_path)

    # replace string
    replace_string(source=path + '/views.py',
                   dest=path + '/views_temp.py',
                   tpl_string='{{OBJECT}}',
                   new_string=api_name)


def replace_string(source, dest, tpl_string, new_string):
    with open(source, "rt") as fin:
        with open(dest, "wt") as fout:
            for line in fin:
                fout.write(
                    line.replace(tpl_string, new_string))

    # rename
    move(dest, source)

    return True
