#!/usr/bin/env bash

read -p "Name of project?: " name

git status
git add *
git commit -m "$name"
git push origin

