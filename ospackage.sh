#!/bin/bash

fpm -s dir -t deb -n faceit -v 0.$BUILD_NUMBER -d "python,python-dev,apache2" $WORKSPACE/faceit=/var/sites/
