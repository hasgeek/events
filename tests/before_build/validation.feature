Feature: Validating data
  Scenario: New event added to events.yml
	Given an event added
	Then events.yml must exist
	Then all mandatory event fields must exist
  Then all mandatory event page fields must exist
	Then all event fields must be the right type and length
  Scenario: New conference added to conferences.yml
	Given a conference added
	Then conferences.yml must exist
	Then all mandatory conference fields must exist
	Then all conference fields must be the right type and length
	Scenario: Events exist in respective folders
	Given event files exist
		| event         |
		| 50p           |
		| anthillinside |
		| fifthelephant |
		| fragments     |
		| jsfoo         |
		| metarefresh   |
		| reactfoo      |
		| rootconf      |
	Then all files should have .md extension
