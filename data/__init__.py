import fnmatch
import os
from ruamel.yaml import YAML

yaml = YAML(typ='safe')


ALL_EVENTS = {}

ALL_BRANDS = yaml.load(open("./data/brands.yml", "r"))

ALLOWED_EVENT_TYPES = yaml.load(open("./data/event-types.yml", "r"))

ALLOWED_CITIES = yaml.load(open("./data/cities.yml", "r"))

ALLOWED_TAGS = yaml.load(open("./data/tags.yml", "r"))



for brand_key in ALL_BRANDS.keys():
    matches = []
    for root, dirnames, filenames in os.walk('./data/_'+brand_key+"_events"):
        for filename in fnmatch.filter(filenames, '*.md'):
            matches.append(os.path.join(root, filename))

    for event_file in matches:
        stream = open(event_file, "r")
        for event in yaml.load_all(stream):
            if event is not None:
                ALL_EVENTS[brand_key+'_'+event_file.rsplit('/', 1)[1].split('.', 1)[0]] = event





