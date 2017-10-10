# -*- coding: utf-8 -*-

from flask import abort, render_template
from helpers import get_brand
from .. import app
from data import ALL_EVENTS



ctx = {
    "title": "HasGeek",
    "colors": {
        "primary": "#444444",
        "accent": "#888888"
    },
    "meta": {
        "title": "title",
        "image": "",
        "description": "this is a description",
        "keywords": "Keywords",
        "favicon": "",
        "og": {
            "url": "",
            "image": "",
            "description": "",
            "title": "title",
            "site_name": "",
            "see_also": "",
            "type": "",
        },
        "twitter": {
            "card": "",
            "url": "",
            "title": "",
            "description": "",
            "image": ""
        },
        "manifest": ""
    }
}



@app.route('/')
@get_brand
def index(brand=None, brand_key=None):
    events = [event for event_key, event in ALL_EVENTS.iteritems() if brand_key in event_key]
    return render_template('pages/index.html.jinja2', events=events, page=events[0], ctx=ctx)


@app.route('/<id>')
@get_brand
def event_page(id, brand=None, brand_key=None):
    print brand_key + id
    event = next((event for event_key, event in ALL_EVENTS.iteritems() if brand_key+'_'+id == event_key), None)
    if event:
        return event['title']
    else:
        return abort(404)


@app.route('/manifest.json')
@get_brand
def manifest_json(id, brand=None, brand_key=None):
    return "{}"

@app.route('/events.ics')
@get_brand
def ical_feed(id, brand=None, brand_key=None):
    return ""