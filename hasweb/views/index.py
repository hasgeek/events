# -*- coding: utf-8 -*-

from flask import abort, render_template
from hasweb.models import Event
from helpers import get_brand
from .. import app
from data import ALL_EVENTS


@app.route('/')
@get_brand
def index(brand=None, brand_key=None):
    events = [event for event_key, event in ALL_EVENTS.iteritems() if brand_key in event]
    return render_template('index.html', events=events)


@app.route('/<id>')
@get_brand
def event_page(id, brand=None, brand_key=None):
    print brand_key + id
    event = next((event for event_key, event in ALL_EVENTS.iteritems() if brand_key+'_'+id == event_key), None)
    if event:
        return event['title']
    else:
        return abort(404)
