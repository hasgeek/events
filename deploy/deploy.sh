#!/bin/sh

set -e

openssl aes-256-cbc -K $encrypted_f874a539f83d_key -iv $encrypted_f874a539f83d_iv -in deploy/id_rsa.enc -out /tmp/deploy_rsa_$1 -d

eval "$(ssh-agent -s)"

chmod 600 /tmp/deploy_rsa_$1

ssh-add /tmp/deploy_rsa_$1

bundle exec jekyll build --config configs/$1_config.yml

cp deploy/gulpfile.js _site/$1
cp deploy/package.json _site/$1
cp .gitignore _site/$1

cd _site/$1


npm install --global gulp-cli
npm install

npm link lru-cache

# gulp generate-service-worker

git init

git config user.name "Deployment Bot (from Travis CI)"
git config user.email "deploy@travis-ci.org"

git add .

git commit -m "Deployment"

git remote add deploy git@e2e.hasgeek.com:$1

git push -u -f deploy master
