# -*- coding: utf-8 -*-

import os.path
from flask import render_template, redirect, url_for, request
from .. import app
from hasweb.models import Event


@app.route('/')
def index():
    event = Event.query.first()
    return "Hello \n"+request.headers['Host']+"---"+event.title
