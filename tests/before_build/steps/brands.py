from behave import *
from ruamel.yaml import YAML
from cerberus import Validator
from data.validators import brand_schema
import datetime
import urllib2
import re

url_regex = re.compile(
    r'^(?:http)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

color_regex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$', re.IGNORECASE)

yaml = YAML(typ='safe')

@given('a brand added')
def step_impl(context):
    pass


@then('brands.yml must exist')
def step_impl(context):
    stream = open("data/brands.yml", "r")
    brands = yaml.load(stream)
    assert isinstance(brands, dict), "brands.yml must be a dict"
    context.brands = brands

    stream = open("data/cities.yml", "r")
    context.cities = yaml.load(stream)


@then('all mandatory brand fields must exist')
def step_impl(context):
    v = Validator(brand_schema)
    for brand_id, brand in context.brands.iteritems():
        assert v.validate(brand), str(v.errors) + " in validating " + brand_id


