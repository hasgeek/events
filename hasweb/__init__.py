# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

import coaster.app
from threading import Lock
from baseframe import baseframe, assets, Version
from flask import Flask, Markup
from flask_lastuser import Lastuser
from flask_lastuser.sqlalchemy import UserManager
from flask_migrate import Migrate
from jinja2 import StrictUndefined
from markdown import Markdown

from ._version import __version__


class DomainDispatcher(object):
    def __init__(self, hosts, hg_app, eventapp):
        self.hosts = set(hosts)
        self.lock = Lock()
        self.hg_app = hg_app
        self.eventapp = eventapp

    def get_application(self, host):
        if ':' in host:  # Remove port number
            host = host.split(':', 1)[0]
        with self.lock:
            if host in self.hosts:
                return self.hg_app
            else:
                return self.eventapp

    def __call__(self, environ, start_response):
        app = self.get_application(environ['HTTP_HOST'])
        return app(environ, start_response)


version = Version(__version__)
hg_app = Flask(__name__, instance_relative_config=True)
event_app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

if hg_app.debug:
    hg_app.jinja_env.undefined = StrictUndefined

if event_app.debug:
    event_app.jinja_env.undefined = StrictUndefined

assets['hasweb.css'][version] = 'css/app.css'
assets['bulma.css'][version] = 'css/main.css'

from . import models, views  # NOQA

@baseframe.app_template_filter('markdown_safe')
def field_markdown(field):
    html = Markdown(safe_mode=False).convert(field)
    return Markup(html)

# Configure the app
coaster.app.init_app(hg_app)
coaster.app.init_app(event_app)
migrate = Migrate(hg_app, models.db)
migrate = Migrate(event_app, models.db)
baseframe.init_app(hg_app, requires=['fontawesome', 'ractive', 'bulma', 'hasweb'], theme='mui')
baseframe.init_app(event_app, requires=['fontawesome', 'ractive', 'bulma', 'hasweb'], theme='mui')
lastuser.init_app(hg_app)
lastuser.init_app(event_app)
lastuser.init_usermanager(UserManager(models.db, models.User))




import data

application = DomainDispatcher(["hasgeek.com", "hasgeek.karthik.dev"], hg_app, event_app)
