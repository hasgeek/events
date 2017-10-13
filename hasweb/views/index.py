# -*- coding: utf-8 -*-

from flask import abort, render_template, jsonify
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
    event = next((event for event_key, event in ALL_EVENTS.iteritems() if brand_key + '_' + id == event_key), None)
    if event is None:
        return abort(404)

    return render_template("pages/event.html.jinja2", event=event, ctx=ctx)


@app.route('/manifest.json')
@get_brand
def manifest_json(brand=None, brand_key=None):
    manifest = {
        "name": "name",  # site name
        "short_name": "short_name",  # if the name is too long
        "display": "standalone",  #
        "orientation": "portrait",
        "start_url": "",
        "theme_color": "",
        "background_color": "",
        "description": "",
        "icons": [
            {
                "src": "launcher-icon-1x.png",
                "type": "image/png",
                "sizes": "48x48"
            },
            {
                "src": "launcher-icon-2x.png",
                "type": "image/png",
                "sizes": "96x96"
            },
            {
                "src": "launcher-icon-4x.png",
                "type": "image/png",
                "sizes": "192x192"
            }
        ],
    }

    return jsonify(manifest)


@app.route('/events.ics')
@get_brand
def ical_feed(id, brand=None, brand_key=None):
    return ""


def build_site_context(brand, event):
    pass


def build_manifest(brand):
    pass