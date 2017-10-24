import re
from ruamel.yaml import YAML
from data import Event

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


ALLOWED_CITIES = yaml.load(open("./data/cities.yml", "r"))

ALLOWED_TAGS = yaml.load(open("./data/tags.yml", "r"))

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
    'maxlength': 80,
    'required': True
}

brand_schema = {
    'title': title_schema,
    'subtitle': subtitle_schema,
    'path': {
        'type': 'string',
        'required': True
    },
    'hostname': {
        'type': 'string',
        'required': True
    },
    'ga_tracking_code': {
        'type': 'string',
        'required': False
    },

    'colors': {
        'type': 'dict',
        'schema': {
            'primary': {
                'validator': valid_color,
                'required': True
            },
            'accent': {
                'validator': valid_color,
                'required': True
            }
        },
        'required': False
    },
    'seo': {
        'type': 'dict',
        'schema': {
            'description': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },
    'meta': {
        'type': 'dict',
        'schema': {
            'image': {
                'type': 'string',
                'required': True
            }
        },
        'required': False
    },
    'icons': {
        'type': 'dict',
        'schema': {
            'touch': {
                'type': 'list',
                'required': True
            }
        },
        'required': False
    }
}

event_schema = {
    'type': {
        'type': 'string',
        'allowed': Event.TYPES
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
    'tags': {
        'type': 'list',
        'allowed': ALLOWED_TAGS,
        'required': False
    },
    'description': {
        'type': 'string',
        'required': True
    },
    'seo': {
        'type': 'dict',
        'schema': {
            'description': {
                'type': 'string',
                'required': True
            },
            'canonical': {
                'validator': valid_external_url,
                'required': True
            }
        },
        'required': False
    },
    'boxoffice': {
        'type': 'dict',
        'schema': {
            'item_collection': {
                'type': 'string',
                'required': True
            },
            'item_ids': {
                'type': 'list',
                'required': False
            }
        },
        'required': False
    },
    'schedules': {
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
            'text': {
                'type': 'string',
                'required': True
            }
        },
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

    'boxoffice_item_collection': {
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

    'related_events': {
        'type': 'list',
        'required': False
    },

    'canonical': {
        'type': 'string',
        'required': False
    }

}
