#!/bin/bash
sleep 5
/usr/local/bin/gunicorn mathsocwebsite.wsgi:application -w 2 -b :8000
