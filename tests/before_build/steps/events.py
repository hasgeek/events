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
	context.cities = yaml.load(stream, Loader=yaml.BaseLoader)

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
		assert len(event.get('name')) < 80, "'name' value is more than 80 characters"
		assert len(event.get('title')) < 80, "'title' value is more than 80 characters"
		assert event.get('city') in context.cities, "'city' value should be one of those listed in cities.yml"
		assert len(event.get('venue')) < 40, "'venue' value is more than 40 characters"


		assert isinstance(datetime.datetime.strptime(event.get('start_time'), '%Y-%m-%d %H:%M'), datetime.datetime), "'start_time' needs to be in the datetime format"
		assert isinstance(datetime.datetime.strptime(event.get('end_time'), '%Y-%m-%d %H:%M'), datetime.datetime), "'end_time' needs to be in the datetime format"
		
		assert event.get('start_time') <= event.get('end_time', datetime.date), "'start_time' needs to before 'end_time'"		

		assert len(event.get('blurb')) < 300 , "'blurb' value is more than 300 characters"
		assert urlregex.match(event.get('url')), "'url' is not a valid URL"

