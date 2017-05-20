Feature: Validating events data
  Scenario: New event added to events.yml
	Given An event added
	Then events.yml must exist
	Then All mandatory fields must exist
	Then All fields must be the right type and length