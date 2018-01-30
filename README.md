# HasGeek Events

A database of tech events in India.


## What kind of events can be listed?
(This is subject to change)

* Developer-focused events in India


## How do add my event?
Add your event details to the `_data/events.yml` file and send a Pull Request to this repository.

Travis will build the branch and run some tests to make sure the data is in the right format and all the mandatory fields exists.

The fields are as follows (all mandatory):


* name: short-hand-name-with-hyphens
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

## Build instructions

Start by cloning this repository into your computer 

`git clone https://github.com/hasgeek/events.git`

Install `rbenv` to manage your local ruby version. If you haven't configured this, you'll get write permission errors on MacOS as Apple has implemented System Integrity Protection, preventing write access to certain system files.

`rbenv` can be install by running `brew install rbenv` if you have homebrew installed, otherwise run 
`curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash`

Run `rbenv version` to check which version of Ruby you're running. If it returns system, you'll need to install or switch to a version of Ruby for local use. 

This repo needs ruby version 2.3.3, therefore run `rbenv install 2.3.3`.

Switch to ruby 2.3.3 to use locally, `rbenv local 2.3.3`

Run `gem install bundler` to install the ruby gem bundler

Navigate to the cloned repository with `cd`. if you cloned it in Documents, you'll get there with `cd Documents/events`. 

Run `bundle install` to let the bundler automatically install all required packages for the build.

Go grab a cup of coffee while this is running, it could take a while. Next, when you're in the `events` folder, run `bundle exec jekyll serve`. This will create a local server for you, which can be accessed by typing `http://localhost:4000/events/`

Ta-da!
