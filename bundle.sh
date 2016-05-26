#!/bin/bash

rsync -r --exclude venv /var/www/ /var/app

cd /var/app

virtualenv venv

source venv/bin/activate

sudo pip install -r requirements.txt

fpm -s dir -t deb -n faceit -v 0.1 -d "python,python-dev,apache2" /var/app/faceit=/var/sites/
