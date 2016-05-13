#!/bin/bash
# Ensure virtualenv exists
pip install virtualenv

virtualenv venv


source ./venv/bin/activate

pip install -r requirements.txt

cd faceit

python manage.py manage.py --noinput
python manage.py collectstatic --noinput
python manage.py test
