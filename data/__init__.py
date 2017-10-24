import fnmatch
import os
from ruamel.yaml import YAML
from models import Event
import IPython

yaml = YAML(typ='safe')


ALL_EVENTS = {}

ALL_BRANDS = yaml.load(open("./data/brands.yml", "r"))

ALLOWED_EVENT_TYPES = yaml.load(open("./data/event-types.yml", "r"))

ALLOWED_CITIES = yaml.load(open("./data/cities.yml", "r"))

ALLOWED_TAGS = yaml.load(open("./data/tags.yml", "r"))

ALL_BRANDS_BY_HOSTNAME = {}



for brand_id, brand in ALL_BRANDS.iteritems():

    ALL_BRANDS_BY_HOSTNAME[brand['hostname']] = brand

    matches = []
    for root, dirnames, filenames in os.walk('./data/_'+brand_id+"_events"):
        for filename in fnmatch.filter(filenames, '*.md'):
            matches.append(os.path.join(root, filename))
    ALL_BRANDS[brand_id]['events']={}
    for event_file in matches:
        stream = open(event_file, "r")
        for event in yaml.load_all(stream):
            if event is not None:
                event_id = event_file.rsplit('/', 1)[1].split('.', 1)[0]
                ALL_BRANDS[brand_id]['events'][event_id] = Event(id=event_id, brand_id=brand_id, **event)

models.ALL_BRANDS = ALL_BRANDS
