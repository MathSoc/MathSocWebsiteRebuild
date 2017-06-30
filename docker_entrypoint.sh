#!/bin/sh
sleep 5
/usr/local/bin/gunicorn mathsocwebsite.wsgi:application --reload -w 2 -b :8000
