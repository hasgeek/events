# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from hasweb import app
from coaster.sqlalchemy import IdMixin, TimestampMixin, BaseMixin, BaseNameMixin

db = SQLAlchemy(app)

from .user import *
from .event import *
