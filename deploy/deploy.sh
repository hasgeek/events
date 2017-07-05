#!/bin/sh

openssl aes-256-cbc -K $encrypted_f874a539f83d_key -iv $encrypted_f874a539f83d_iv -in deploy/id_rsa.enc -out /tmp/deploy_rsa -d

eval "$(ssh-agent -s)"

chmod 600 /tmp/deploy_rsa

ssh-add /tmp/deploy_rsa

cd _site

git init

git add .

git remote add deploy git@e2e.hasgeek.com:fragments

git push deploy
