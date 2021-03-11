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