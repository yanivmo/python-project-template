#!/usr/bin/env sh

echo "Running Black"
poetry run black .

echo "\nRunning flake8"
poetry run flake8 . && echo "Done."
