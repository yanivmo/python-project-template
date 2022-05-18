#!/usr/bin/env sh

echo "Running Black"
pipenv run black .

echo "\nRunning flake8"
pipenv run flake8 . && echo "Done."
