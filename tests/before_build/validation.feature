Feature: Validating data
  Scenario: New event added to events.yml
	Given an event added
	Then events.yml must exist
	Then all mandatory event fields must exist
	Then all event fields must be the right type and length
  Scenario: New brand added to conferences.yml
	Given a brand added
	Then brands.yml must exist
	Then all mandatory brand fields must exist