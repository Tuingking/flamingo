#! /usr/bin/env python
"""Manager
Automaticaly create or drop database with single command.
This module depend on flask-script
"""
import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from flamingo.commands.keygen import Keygen
from flamingo.commands.routes import Routes
from flamingo.commands.blueprint.make_api import MakeApi
from flamingo.commands.blueprint.make_blueprint import MakeBlueprint


"""
set environment by:
$ export FLASKF_ENV=dev
"""
app = create_app(os.getenv('FLASKF_ENV') or 'dev')
manager = Manager(app)


migrate = Migrate(app, db)

# Register command
manager.add_command('db', MigrateCommand)
manager.add_command('keygen', Keygen)
manager.add_command('routes', Routes)
manager.add_command('api', MakeApi)
manager.add_command('bp', MakeBlueprint)

if __name__ == '__main__':
    manager.run()
