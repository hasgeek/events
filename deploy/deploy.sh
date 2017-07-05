#!/bin/sh

openssl aes-256-cbc -K $encrypted_f874a539f83d_key -iv $encrypted_f874a539f83d_iv -in deploy/id_rsa.enc -out /tmp/deploy_rsa_$1 -d

eval "$(ssh-agent -s)"

chmod 600 /tmp/deploy_rsa_$1

ssh-add /tmp/deploy_rsa_$1

bundle exec jekyll build --config configs/$1_config.yml
cd _site/$1

git init

git config user.name "Deployment Bot (from Travis CI)"
git config user.email "deploy@travis-ci.org"

git add .

git commit -m "Deployment"

git remote add deploy git@e2e.hasgeek.com:$1

git push -u -f deploy master
