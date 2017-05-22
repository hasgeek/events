Feature: Validating events data
  Scenario: New event added to events.yml
	Given An event added
	Then events.yml must exist
	Then all mandatory fields must exist
	Then all fields must be the right type and length