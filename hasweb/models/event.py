# -*- coding: utf-8 -*-

from coaster.sqlalchemy import IdMixin
from . import db

__all__ = ['Event']


class Map(IdMixin, db.Model):
    __tablename__ = 'map'
    LEAFLET = 1
    MAPBOX = 2
    def __init__(self, style=LEAFLET, access_token=None):
        self.style = style
        self.access_token = access_token


class Event(IdMixin, db.Model):
    __tablename__ = 'event'
    CONFERENCE = 0
    WORKSHOP = 1
    MEETUP = 2
    title = db.Column(db.String(80), unique=True)

    def __init__(self, type=None, title=None, datelocation=None, subtitle=None, city=None, start_time=None, end_time=None, description=None, tickets=None, schedule=None, logo=None, funnel=None, subbanner=None, venue=None, livestream=None, announcements=None, related_events=None, overview=None, featured_speakers=None, sponsor=None):
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


class Venue(IdMixin, db.Model):
    __tablename__ = 'venue'
    def __init__(self, label=None, address=None, lat=None, lng=None, google_maps_url=None, map=map):
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
