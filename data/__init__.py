import fnmatch
import os
from ruamel.yaml import YAML

yaml = YAML(typ='safe')




matches = []
for root, dirnames, filenames in os.walk('./hasweb/data/'):
    for filename in fnmatch.filter(filenames, '*.md'):
        matches.append(os.path.join(root, filename))



for event_file in matches:
    stream = open(event_file, "r")

    for event in yaml.load_all(stream):
        print event




