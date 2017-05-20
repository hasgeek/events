from behave import *
import yaml
import datetime
import urllib2

@given('An event added')
def step_impl(context):
	pass

@then('events.yml must exist')
def step_impl(context):
	stream = open("_data/events.yml", "r")
	events = yaml.load(stream)
	assert isinstance(events, list)
	context.events = events

@then('All mandatory fields must exist')
def step_impl(context):
	for event in context.events:
		print("Checking mandatory fields for " + event['name'])
		assert event.get('name'), "'name' value is missing"
		assert event.get('title'), "'title' value is missing"
		assert event.get('start_time'), "'start_time' value is missing"
		assert event.get('end_time'), "'end_time' value is missing"
		assert event.get('blurb'), "'blurb' value is missing"

@then('All fields must be the right type and length')
def step_impl(context):
	for event in context.events:
		print("Validating fields for " + event['name'])
		assert len(event.get('name')) < 80, "'name' value is more than 80 characters"
		assert len(event.get('title')) < 80, "'title' value value is more than 80 characters"
		assert isinstance(event.get('start_time'), datetime.date), "'start_time' needs to be in the datetime format"
		assert isinstance(event.get('end_time'), datetime.date), "'end_time' needs to be in the datetime format"
		assert len(event.get('blurb')) < 300 , "'blurb' value is more than 200 characters"
		if event.get('url'):
			request = urllib2.Request(event.get('url'))
			request.get_method = lambda : 'HEAD'
			response = urllib2.urlopen(request)
			assert response.code==200, "'url' is not a valid URL"
		if event.get('funnel'):
			request = urllib2.Request(event.get('funnel'))
			request.get_method = lambda : 'HEAD'
			response = urllib2.urlopen(request)
			assert response.code==200, "'funnel' is not a valid URL"

