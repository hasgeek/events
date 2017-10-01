import re

color_regex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$', re.IGNORECASE)

def valid_color(field, value, error):
    if not color_regex.match(value):
        error(field, "Must be a valid color")




brand_schema = {
    'title': {
        'type': 'string',
        'maxlength': 80,
        'required': True
    },
    'subtitle': {
        'type': 'string',
        'maxlength': 160,
        'required': True
    },
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
    'type' : {
        'type': 'string',
        'allowed': ['event', 'workshop', 'meetup', 'online']
    }
}
