# HasGeek Events

A database of tech events in India.


## What kind of events can be listed?
(This is subject to change)

* Developer-focused events in India
* Must have free entry/registration


## How do add my event?
Add your event details to the `_data/events.yml` file and send a Pull Request to this repository.

Travis will build the branch and run some tests to make sure the data is in the right format and all the mandatory fields exists.

The fields are as follows (all mandatory):


* name: short-hand-name-with-underscores
* title: Full name of the event in <80 characters (In [sentence case](https://www.thoughtco.com/sentence-case-titles-1691944))
* city:  A valid city from the list at `_data/cities.yml`
* venue: Venue name in <40 characters
* start_time: YYYY-MM-DD HH:MM (24h format in IST)
* end_time: YYYY-MM-DD HH:MM (24h format in IST)
* url: A link to a valid URL for the event.
* blurb: A short description of the event. Must be <300 characters.


## How will it get approved?
Someone from our team will review the Pull Request once it is sent. All communication will be in public on the PR itself.

## Support
If you have any questions, you can open reach us on the [Friends of HasGeek Slack](https://friends.hasgeek.com) team. Ping @karthik or @dunebuggie there.


## API
(This is work in progress)
You can fetch a list of all the events here [https://hasgeek.github.io/events/api/all.json](https://hasgeek.github.io/events/api/all.json)
