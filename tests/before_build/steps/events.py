from behave import *
from ruamel.yaml import YAML
from cerberus import Validator
from data.validators import event_schema
import datetime
import re, os, fnmatch

urlregex = re.compile(
    r'^(?:http)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

yaml = YAML(typ='safe')


@given('an event added')
def step_impl(context):
    pass


@then('events.yml must exist')
def step_impl(context):
    matches = []
    events = []
    for root, dirnames, filenames in os.walk('./data/'):
        for filename in fnmatch.filter(filenames, '*.md'):
            matches.append(os.path.join(root, filename))

    for event_file in matches:
        stream = open(event_file, "r")

        for event in yaml.load_all(stream):
            if event is not None:
                events.append(event)

    context.events = events


@then('all mandatory event fields must exist')
def step_impl(context):
    v = Validator(event_schema)
    for event in context.events:
        assert v.validate(event), str(v.errors) + " in validating " + event['title']


@then('all event fields must be the right type and length')
def step_impl(context):
    for event in context.events:
        pass
