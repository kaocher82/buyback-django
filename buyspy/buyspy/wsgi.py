"""
WSGI config for buyspy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dj_static import Cling, MediaCling

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "buyspy.settings")

application = Cling(MediaCling(get_wsgi_application()))
