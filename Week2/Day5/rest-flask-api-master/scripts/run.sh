#!/bin/bash
/opt/conda/envs/app/bin/flask db upgrade
exec /opt/conda/envs/app/bin/uwsgi --ini /app/scripts/uwsgi.ini
