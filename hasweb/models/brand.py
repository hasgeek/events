# -*- coding: utf-8 -*-

import re

from coaster.sqlalchemy import IdMixin

import data
from . import db

__all__ = ['EventType', 'MapType', 'Speaker']


url_regex = re.compile(
    r'^(?:http)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class Brand(object):
    def __init__(self, id=None, name=None, config=None):

        self.validate(id, name)

        self.id = id
        self.name = name

    def validate(self, id, name):
        if id == None or name == None:
            raise ValueError("Brand needs an id and name")


class BrandConfig(object):
    def __init__(self, title=None, subtitle=None, description=None, hostname=None, style=None, analytics=None, meta=None):

        self.validate(id, name)

        self.id = id
        self.name = name

    def validate(self, id, name):
        if id == None or name == None:
            raise ValueError("MapType needs an id and name")



class Map(IdMixin, db.Model):
    __tablename__ = 'map'

    type = db.Column(db.Unicode(80), nullable=False)
    lat = db.Column(db.Decimal, nullable=False)
    lng = db.Column(db.Decimal, nullable=False)

    access_token = db.Column(db.Unicode(300), nullable=True)
    styles_url = db.Column(db.Unicode(300), nullable=True)


    def __init__(self, type=None, lat=None, lng=None, access_token=None, styles_url=None):

        self.validate_type(type)
        self.validate_latlng(lat, lng)
        self.validate_access_token(type, access_token)

        self.type = type
        self.lat = lat
        self.lng = lng
        self.access_token = access_token
        self.styles_url = styles_url



    def validate_type(self, type=None):
        if type in data.MAP_TYPES.keys():
            return
        else:
            raise ValueError('Map\'s type is invalid')


    def validate_access_token(self, type=None, access_token=None):
        if type in data.MAP_TYPES.keys():
            if type == 'mapbox' and access_token == None:
                raise ValueError('Need to specify an access token when using mapbox maps')
        else:
            raise ValueError('Invalid maptype')



    def validate_latlng(self, lat=None, lng=None):
        try:
            float(lat)
            float(lng)
        except Exception as e:
            raise ValueError('Map\'s Lat or Lng are invalid')



class TicketConfig(IdMixin, db.Model):
    __tablename__ = 'ticket_config'

    BOXOFFICE = 0

    type = db.Column(db.SmallInteger, nullable=False)



class Venue(IdMixin, db.Model):
    __tablename__ = 'venue'

    def __init__(self, label=None, address=None, lat=None, lng=None, google_maps_url=None, map=None):
        self.label = label
        self.address = address
        self.lat = lat
        self.lng = lng
        self.google_maps_url = google_maps_url
        self.map = map


class Speaker(IdMixin, db.Model):
    __tablename__ = 'speaker'

    def __init__(self):
        pass

class Sponsor(IdMixin, db.Model):
    __tablename__ = 'sponsor'

    def __init__(self):
        pass


class SponsorshipDeck(IdMixin, db.Model):
    __tablename__ = 'sponsorship_deck'

    def __init__(self, blurb=None, label=None, url=None):
        self.blurb = blurb
        self.label = label
        self.url = url


class Event(IdMixin, db.Model):
    __tablename__ = 'event'

    title = db.Column(db.Unicode(80))
    subtitle = db.Column(db.Unicode(80))
    datelocation = db.Column(db.Unicode(80))
    city = db.Column(db.Unicode(80))
    start_time = db.Column(db.DateTime())
    end_time = db.Column(db.DateTime())
    description = db.Column(db.Unicode(300))


    register_config_id = db.Column(None, db.ForeignKey('register_config.id'))
    register_config = db.relationship("RegisterConfig", backref=db.backref("event", uselist=False))

    event_type_id = db.Column(None, db.ForeignKey('event_type.id'))
    event_type = db.relationship("EventType", backref=db.backref("event", uselist=False))



    def __init__(self, type=None, title=None, subtitle=None, datelocation=None, city=None, start_time=None,
                 end_time=None, description=None, tickets=None, schedule=None, logo=None, funnel=None, subbanner=None,
                 venue=None, livestream=None, announcements=None, related_events=None, overview=None,
                 featured_speakers=None, sponsor=None):
        self.type = type
        self.title = title
        self.datelocation = datelocation
        self.subtitle = subtitle
        self.city = city
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.tickets = tickets
        self.schedule = schedule
        self.logo = logo
        self.funnel = funnel
        self.subbanner = subbanner
        self.venue = venue
        self.livestream = livestream
        self.announcements = announcements
        self.related_events = related_events
        self.overview = overview
        self.featured_speakers = featured_speakers
        self.sponsor = sponsor