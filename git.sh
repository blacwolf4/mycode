#!/usr/bin/env bash

read name

git add *
git commit -m "$name"
git push origin
