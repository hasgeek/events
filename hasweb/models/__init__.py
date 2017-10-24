# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from hasweb import app

db = SQLAlchemy(app)

from .user import *