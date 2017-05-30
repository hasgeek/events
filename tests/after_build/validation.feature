Feature: Validating APIs
  Scenario: New event added to events.yml and jekyll has built
	Given an event added and jekyll has built
	Then /api/conferences.json should be correct
	Then /api/events.json should be correct
	Then /api/cities.json should be correct
	Then /api/all.json should be correct