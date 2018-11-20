#!/bin/bash
RUN echo yes | python /app/manage.py collectstatic
python /app/manage.py makemigrations
python /app/manage.py migrate
gunicorn buyspy.wsgi --chdir /app/ --bind 0.0.0.0:8000


#
