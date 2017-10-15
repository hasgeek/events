# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

import coaster.app
from coaster.gfm import markdown_convert_text
from baseframe import baseframe, assets, Version
from flask import Flask, Markup
from flask_lastuser import Lastuser
from flask_lastuser.sqlalchemy import UserManager
from flask_migrate import Migrate
from jinja2 import StrictUndefined

from ._version import __version__

version = Version(__version__)
app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

if app.debug:
    app.jinja_env.undefined = StrictUndefined

assets['hasweb.css'][version] = 'css/app.css'
assets['bulma.css'][version] = 'css/main.css'

from . import models, views  # NOQA

@baseframe.app_template_filter('mdown')
def field_markdown(field):
    html = markdown_convert_text(field)
    return Markup(html)

# Configure the app
coaster.app.init_app(app)
migrate = Migrate(app, models.db)
baseframe.init_app(app, requires=['fontawesome', 'ractive', 'bulma', 'hasweb'], theme='mui')
lastuser.init_app(app)
lastuser.init_usermanager(UserManager(models.db, models.User))


import data
