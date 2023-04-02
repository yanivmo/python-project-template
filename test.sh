#!/usr/bin/env sh
ENV_FOR_DYNACONF=testing DYNACONF_PROMPT__WORLD='World!!!' poetry run python -m pytest --verbose tests
