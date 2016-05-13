#!/bin/bash

source ./venv/bin/activate
cd faceit
python manage.py test
