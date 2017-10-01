# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

import coaster.app
from baseframe import baseframe, assets, Version
from flask import Flask
from flask_lastuser import Lastuser
from flask_lastuser.sqlalchemy import UserManager
from flask_migrate import Migrate

from ._version import __version__

version = Version(__version__)
app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

assets['hasweb.css'][version] = 'css/app.css'
assets['bulma.css'][version] = 'css/main.scss'

from . import models, views  # NOQA

# Configure the app
coaster.app.init_app(app)
migrate = Migrate(app, models.db)
baseframe.init_app(app, requires=['fontawesome', 'ractive', 'bulma', 'hasweb'])
lastuser.init_app(app)
lastuser.init_usermanager(UserManager(models.db, models.User))

