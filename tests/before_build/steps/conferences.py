from behave import *
import yaml
import datetime
import urllib2
import re

urlregex = re.compile(
    r'^(?:http)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

colorregex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$', re.IGNORECASE)

@given('a conference added')
def step_impl(context):
	pass

@then('conferences.yml must exist')
def step_impl(context):
	stream = open("_data/conferences.yml", "r")
	conferences = yaml.load(stream, Loader=yaml.BaseLoader)
	assert isinstance(conferences, list), "conferences.yml must be a list"
	context.conferences = conferences

	stream = open("_data/cities.yml", "r")
	context.cities = yaml.load(stream)

@then('all mandatory conference fields must exist')
def step_impl(context):
	for conf in context.conferences:
		print("Checking mandatory fields for " + conf['name'])
		assert conf.get('name'), "'name' value is missing"
		assert conf.get('title'), "'title' value is missing"
		assert conf.get('city'), "'city' value is missing"
		assert conf.get('venue'), "'venue' value is missing"
		assert conf.get('start_time'), "'start_time' value is missing"
		assert conf.get('end_time'), "'end_time' value is missing"
		assert conf.get('blurb'), "'blurb' value is missing"
		if conf.get('color'):
			assert conf.get('color').get('primary'), "'primary' color is not set"
			assert conf.get('color').get('primary_dark'), "'primary_dark' color is not set"
			assert conf.get('color').get('accent'), "'accent' color is not set"

@then('all conference fields must be the right type and length')
def step_impl(context):
	for conf in context.conferences:
		print("Validating fields for " + conf['name'])
		assert len(conf.get('name')) < 80, "'name' value is more than 80 characters"
		assert len(conf.get('title')) < 80, "'title' value is more than 80 characters"
		assert conf.get('city') in context.cities, "'city' value should be one of those listed in cities.yml"
		assert len(conf.get('venue')) < 40, "'venue' value is more than 40 characters"
		if conf.get('google_maps_pin'):
			assert urlregex.match(conf.get('google_maps_pin')), "'google_maps_pin' is not a valid URL"
		assert isinstance(datetime.datetime.strptime(conf.get('start_time'), '%Y-%m-%d'), datetime.datetime), "'start_time' needs to be in the datetime format"
		assert isinstance(datetime.datetime.strptime(conf.get('end_time'), '%Y-%m-%d'), datetime.datetime), "'end_time' needs to be in the datetime format"
		assert datetime.datetime.strptime(conf.get('start_time'), '%Y-%m-%d') <= datetime.datetime.strptime(conf.get('end_time'), '%Y-%m-%d'), "'start_time' needs to before 'end_time'"
		assert len(conf.get('blurb')) < 300 , "'blurb' value is more than 300 characters"
		if conf.get('url'):
			assert urlregex.match(conf.get('url')), "'url' is not a valid URL"
		if conf.get('funnel'):
			assert urlregex.match(conf.get('funnel')), "'funnel' is not a valid URL"

		if conf.get('color'):
			assert colorregex.match(conf.get('color').get('primary')), "'primary' color is not a valid color"
			assert colorregex.match(conf.get('color').get('primary_dark')), "'primary_dark' color is not a valid color"
			assert colorregex.match(conf.get('color').get('accent')), "'accent' color is not a valid color"
