# -*- coding: utf-8 -*-

import re


url_regex = re.compile(
    r'^(?:http)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


"""
fifthelephant:
  title: The Fifth Elephant
  meta:
    description: "India’s most renowned data science conference. Discuss the most cutting edge developments in the fields of machine learning, data science and technology that power data collection and analysis."
    short_description: "India's most renowned data science community and conference"
    
  path: "" # the subpath of your site, e.g. /blog
  hostname: "fifthelephant.in" # the base hostname & protocol for your site, e.g. http://example.com
  colors:
    primary: "#498f94"
    accent: "#EC6015"
  ga_tracking_code: UA-19123154-20
  meta:
    image: "images/meta/fifthelephant.png"
  icons:
    touch:
    - src: "images/touch/fifthelephant-icon-192.png"
      sizes: "192x192"
      type: "image/png"
"""


class Brand(object):
    def __init__(self, id=None, title=None, description=None, short_description=None, config=None):

        self.validate_id_and_title(id, title)

        self.id = id
        self.title = title
        self.description = description
        self.short_description = short_description
        self.config = BrandConfig(**config)

    def validate_id_and_title(self, id, title):
        if id == None or title == None:
            raise ValueError("Brand needs an id and title")



class BrandConfig(object):
    def __init__(self, hostname=None, style=None, analytics=None, meta=None):
        pass

    def validate(self, id, name):
        if id == None or name == None:
            raise ValueError("BrandConfig needs an id and name")


ALL_BRANDS = {}



class Event(object):

    EVENT = 'event'
    WORKSHOP = 'workshop'
    MEETUP = 'meetup'
    OPEN_HOUSE = 'open-house'

    TYPES = [EVENT, WORKSHOP, MEETUP, OPEN_HOUSE]

    def __init__(self, id=None, type=None, title=None, subtitle=None, datelocation=None, city=None, start_time=None,
                 end_time=None, description=None, tickets=None, schedule=None, logo=None, funnel=None, subbanner=None,
                 venue=None, livestream=None, announcements=None, related_events=None, overview=None,
                 featured_speakers=None, speakers=None, instructors=None, sponsor=None, accommodation=None, footer=None, boxoffice_item_collection=None, canonical=None, live=None, brand_id=None):

        self.id = self.validate_id(id=id)
        self.type = self.validate_type(type=type)
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
        self.brand_id = brand_id


    @property
    def url(self):
        return "https://"+self.brand['hostname']+"/"+self.id

    @property
    def brand(self):
        return ALL_BRANDS.get(self.brand_id)

    def validate_id(self, id):
        if id == None:
            raise ValueError("Event needs a url")
        return id

    def validate_type(self, type):
        if type == None:
            raise ValueError("Event needs a type")
        if type not in self.TYPES:
            raise ValueError("Event type needs to be one of: "+str(self.TYPES))
        return type


    @staticmethod
    def get_by_event_id_and_brand_id(event_id=None, brand_id=None):
        if ALL_BRANDS.get(brand_id) is None:
            return None
        if ALL_BRANDS.get(brand_id)['events'].get(event_id) is None:
            return None
        return ALL_BRANDS.get(brand_id)['events'].get(event_id)

    @staticmethod
    def get_all_events_by_brand_id(brand_id=None):
        if ALL_BRANDS.get(brand_id) is None:
            return None
        return ALL_BRANDS.get(brand_id)['events']

    @staticmethod
    def url_by_event_id_and_brand_id(event_id=None, brand_id=None):
        if ALL_BRANDS.get(brand_id) is None:
            return None
        if ALL_BRANDS.get(brand_id)['events'].get(event_id) is None:
            return None
        return ALL_BRANDS.get(brand_id)['events'].get(event_id).id

