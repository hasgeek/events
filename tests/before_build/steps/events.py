from behave import *
import datetime
import urllib2
import re
import os
import fnmatch
from ruamel.yaml import YAML
from cerberus import Validator

urlregex = re.compile(
    r'^(?:http)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

color_regex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$', re.IGNORECASE)

url_regex = re.compile(
    r'^(?:http)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

yaml = YAML(typ='safe')


def valid_color(field, value, error):
    if not color_regex.match(value):
        error(field, "Must be a valid color")


def valid_external_url(field, value, error):
    if not url_regex.match(value):
        error(field, "Must be a valid URL")


ALLOWED_CITIES = yaml.load(open("./_data/cities.yml", "r"))

title_schema = {
    'type': 'string',
    'maxlength': 80,
    'required': True
}

subtitle_schema = {
    'type': 'string',
    'maxlength': 160,
    'required': True
}

datelocation_schema = {
    'type': 'string',
    'required': True
}

featured_speakers_schema = {
    'funnel_url': {
        'validator': valid_external_url,
        'required': False
    },
    'talk_title': {
        'type': 'string',
        'required': True
    },
    'name': {
        'type': 'string',
        'required': True
    },
    'image_url': {
        'validator': valid_external_url,
        'required': False
    },
    'website': {
        'type': 'dict',
        'schema': {
            'label': {
                'type': 'string',
                'required': True
            },
            'url': {
                'validator': valid_external_url,
                'required': True
            }
        },
        'required': False
    },
    'blurb': {
        'type': 'string',
        'required': False
    },
}

proposed_speakers_schema = {
    'funnel_url': {
        'validator': valid_external_url,
        'required': False
    },
    'talk_title': {
        'type': 'string',
        'required': True
    },
    'name': {
        'type': 'string',
        'required': True
    },
    'image_url': {
        'validator': valid_external_url,
        'required': False
    },
    'website': {
        'type': 'dict',
        'schema': {
            'label': {
                'type': 'string',
                'required': True
            },
            'url': {
                'validator': valid_external_url,
                'required': True
            }
        },
        'required': False
    },
    'blurb': {
        'type': 'string',
        'required': False
    },
}

flickr_album_schema = {
    'title': {
        'type': 'string',
        'required': False
    },
    'album_url': {
        'validator': valid_external_url,
        'required': True
    }
}

banner_schema = {
    'validator': valid_external_url,
    'required': False
}

youtube_url_schema = {
    'title': {
        'type': 'string',
        'required': False
    },
    'youtube_embed': {
        'validator': valid_external_url,
        'required': True
    }
}

discussions_schema = {
    'funnel_url': {
        'validator': valid_external_url,
        'required': False
    },
    'talk_title': {
        'type': 'string',
        'required': True
    },
    'name': {
        'type': 'string',
        'required': True
    },
    'image_url': {
        'validator': valid_external_url,
        'required': False
    },
    'website': {
        'type': 'dict',
        'schema': {
            'label': {
                'type': 'string',
                'required': True
            },
            'url': {
                'validator': valid_external_url,
                'required': True
            }
        },
        'required': False
    },
    'blurb': {
        'type': 'string',
        'required': False
    },
}

event_schema = {
    'layout': {
        'type': 'string',
        'allowed': ['event', 'workshop', 'sponsorship']
    },
    'title': title_schema,
    'subtitle': subtitle_schema,
    'datelocation': datelocation_schema,
    'city': {
        'type': 'string',
        'allowed': ALLOWED_CITIES
    },
    'start_time': {
        'type': 'date',
        'required': True
    },
    'end_time': {
        'type': 'date',
        'required': True
    },
    'description': {
        'type': 'string',
        'required': True
    },
    'subbanner': {
        'type': 'string',
        'required': False
    },
    'funnel': {
        'type': 'dict',
        'required': False
    },
    'schedule': {
        'type': 'dict',
        'required': False
    },
    'logo': {
        'type': 'dict',
        'schema': {
            'image_url': {
                'type': 'string',
                'required': True
            },
            'has_title': {
                'type': 'boolean',
                'required': False
            }
        },
        'required': False
    },
    'banner': {
        'type': 'string',
        'required': False
    },
    'youtube_url': {
        'type': 'dict',
        'schema': {
            'title': {
                'type': 'string',
                'required': False
            },
            'youtube_embed': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },

    'blog': {
        'type': 'dict',
        'schema': {
            'feed_url': {
                'type': 'string',
                'required': True
            },
            'url': {
                'type': 'string',
                'required': True
            },
            'title': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },
    'hasjob': {
        'type': 'dict',
        'schema': {
            'url': {
                'type': 'string',
                'required': True
            },
            'limit': {
                'type': 'float',
                'required': True
            }
        },
        'required': False
    },

    'hasgeektv-event-playlist-link': {
        'type': 'dict',
          'schema': {
              'url': {
                  'type': 'string',
                  'required': True
              }
          },
          'required': False
    },

    'mailchimp': {
        'type': 'dict',
        'schema': {
            'url': {
                'type': 'string',
                'required': True
            },
            'u': {
                'type': 'string',
                'required': True
            },
            'id': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },
    'venue': {
        'type': 'dict',
        'schema': {
            'label': {
                'type': 'string',
                'required': True
            },
            'mapbox': {
                'type': 'dict',
                'required': False
            },
            'lat': {
                'type': 'float',
                'required': True
            },
            'lng': {
                'type': 'float',
                'required': True
            },
            'address': {
                'type': 'string',
                'required': False
            },
            'google_maps_url': {
                'validator': valid_external_url,
                'required': True
            },
        },
        'required': False
    },
    'livestream': {
        'type': 'list',
        'schema': {
            'title': {
                'type': 'string',
                'required': True
            },
            'youtube_url': {
                'validator': valid_external_url,
                'required': True
            }
        },
        'required': False
    },
    'announcements': {
        'type': 'list',
        'schema': {
            'title': {
                'type': 'string',
                'required': True
            },
            'icon':{
                'validator': valid_external_url,
                'required': True
            },
            'text': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },
    'fixed_announcements': {
        'type': 'list',
        'required': False
    },
    'overview': {
        'type': 'dict',
        'schema': {
            'left_content': {
                'type': 'string',
                'required': False
            },
            'center_content': {
                'type': 'string',
                'required': False
            },
            'right_content': {
                'type': 'string',
                'required': False
            }
        },
        'required': False
    },

    'highlights': {
        'type': 'dict',
        'schema': {
            'left_content': {
                'type': 'string',
                'required': False
            },
            'center_content': {
                'type': 'string',
                'required': False
            },
            'right_content': {
                'type': 'string',
                'required': False
            }
        },
        'required': False
    },

    'boxoffice_item_collection': {
        'type': 'string',
        'required': False
    },

    'boxoffice_item_categories': {
        'type': 'list',
        'required': False
    },

    'outreach_item_collection': {
        'type': 'string',
        'required': False
    },

    'rsvp': {
        'type': 'string',
        'required': False
    },

    'speakers': {
        'type': 'list',
        'required': False
    },

    'footer': {
        'type': 'dict',
        'required': False
    },

    'accommodation': {
        'type': 'dict',
        'required': False
    },

    'instructors': {
        'type': 'list',
        'required': False
    },

    'sponsor': {
        'type': 'dict',
        'required': False
    },

    'funnels': {
        'type': 'dict',
        'schema': {
            'space': {
                'type': 'string',
                'required': True
            },
            'id': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },

    'live': {
        'type': 'list',
        'required': False
    },

    'featured_speakers': {
        'type': 'list',
        'required': False
    },

    'proposed_speakers': {
        'type': 'list',
        'required': False
    },

    'flickr_album': {
        'type': 'dict',
        'schema': {
            'title': {
                'type': 'string',
                'required': False
            },
            'album_url': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },

    'photo_album': {
        'type': 'dict',
        'schema': {
            'title': {
                'type': 'string',
                'required': False
            },
            'photos': {
                'type': 'list',
                'required': True
            }
        },
        'required': False
    },

    'testimonials': {
        'type': 'list',
        'required': False
    },

    'discussions': {
        'type': 'list',
        'required': False
    },

    'related_events': {
        'type': 'list',
        'required': False,
        'schema': featured_speakers_schema
    },

    'featured': {
        'type': 'boolean',
        'required': False
    },

    'featured_image': {
        'type': 'string',
        'validator': valid_external_url,
        'required': False
    },

    'canonical': {
        'type': 'string',
        'required': False
    }

}



@given('an event added')
def step_impl(context):
	pass

@then('events.yml must exist')
def step_impl(context):
    stream = open("_data/events.yml", "r")
    events = yaml.load(stream)
    assert isinstance(events, list), "events.yml must be a list"
    context.events = events
    stream = open("_data/cities.yml", "r")
    context.cities = yaml.load(stream)
    all_events = []
    matches = []
    for root, dirnames, filenames in os.walk('./'):
        for filename in fnmatch.filter(filenames, '*.md'):
            matches.append(os.path.join(root, filename))

    for event_file in matches:
        if "_events" in event_file:
            stream = open(event_file, "r")

            for event in yaml.load_all(stream):
                if event is not None:
                    all_events.append(event)
    context.all_events = all_events

@then('all mandatory event fields must exist')
def step_impl(context):
	for event in context.events:
		print("Checking mandatory fields for " + event['name'])
		assert event.get('name'), "'name' value is missing"
		assert event.get('title'), "'title' value is missing"
		assert event.get('city'), "'city' value is missing"
		assert event.get('venue'), "'venue' value is missing"
		assert event.get('start_time'), "'start_time' value is missing"
		assert event.get('end_time'), "'end_time' value is missing"
		assert event.get('blurb'), "'blurb' value is missing"
		assert event.get('url'), "'url' value is missing"

@then('all event fields must be the right type and length')
def step_impl(context):
	for event in context.events:
		print("Validating fields for " + event['name'])
		assert len(event.get('name')) <= 80, "'name' value is more than 80 characters"
		assert len(event.get('title')) <= 80, "'title' value is more than 80 characters"
		assert event.get('city') in context.cities, "'city' value should be one of those listed in cities.yml"
		assert len(event.get('venue')) <= 40, "'venue' value is more than 40 characters"


		assert isinstance(datetime.datetime.strptime(event.get('start_time'), '%Y-%m-%d %H:%M'), datetime.datetime), "'start_time' needs to be in the datetime format"
		assert isinstance(datetime.datetime.strptime(event.get('end_time'), '%Y-%m-%d %H:%M'), datetime.datetime), "'end_time' needs to be in the datetime format"

		assert event.get('start_time') <= event.get('end_time', datetime.date), "'start_time' needs to before 'end_time'"

		assert len(event.get('blurb')) <= 300 , "'blurb' value is more than 300 characters"
		assert urlregex.match(event.get('url')), "'url' is not a valid URL"


@then('all mandatory event page fields must exist')
def step_impl(context):
    v = Validator(event_schema)
    for event in context.all_events:
        assert v.validate(event), str(v.errors) + " in validating " + event['title']

@given('event files exist')
def step_impl(context):
    folder_list = getattr(context, "folder_list", None)
    if not folder_list:
        context.folder_list = []
    for row in context.table:
        events_folder = "_" + row['event'] + "_events"
        context.folder_list.append(events_folder)
    pass

@then('all files should have .md extension')
def step_impl(context):
    print(context)
    for event_folder in context.folder_list:
        for filename in os.listdir(event_folder):
            assert filename.endswith(".md"), filename + " should end with .md"
