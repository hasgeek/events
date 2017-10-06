# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, request
from hasweb.models import Event
from helpers import get_brand
from .. import app
from data import ALL_EVENTS


@app.route('/event/<id>')
@get_brand
def index(id, brand=None):
    return brand['title'] or "Hello"
