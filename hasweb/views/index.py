# -*- coding: utf-8 -*-

import os.path
from flask import render_template, redirect, url_for, request
from .. import app
from hasweb.models import Event


@app.route('/', subdomain="<brand>")
def index(brand):
    event = Event.query.one()
    return "Hello "+brand+"\n"+request.headers['Host']+"---"+event.title
