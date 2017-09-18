#!/usr/bin/env python

from coaster.manage import init_manager

import hasweb
import hasweb.models as models
import hasweb.forms as forms
import hasweb.views as views
from hasweb.models import db
from hasweb import app


if __name__ == '__main__':
    db.init_app(app)
    manager = init_manager(app, db, hasweb=hasweb, models=models, forms=forms, views=views)
    manager.run()
