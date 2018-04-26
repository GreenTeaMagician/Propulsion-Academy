#!/bin/bash
python manage.py migrate
python manage.py collectscript
exec /opt/conda/envs/app/bin/uwsgi --ini /scripts/uwsgi.ini