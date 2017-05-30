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

@given('an event added and jekyll has built')
def step_impl(context):
	pass

@then('/api/conferences.json should be correct')
def step_impl(context):
	pass

@then('/api/events.json should be correct')
def step_impl(context):
	pass

@then('/api/cities.json should be correct')
def step_impl(context):
	pass

@then('/api/all.json should be correct')
def step_impl(context):
	pass
