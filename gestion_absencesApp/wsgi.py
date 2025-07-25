"""
WSGI config for gestion_absencesApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


settings_module = 'gestion_absencesApp.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'gestion_absencesApp.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_absencesApp.settings')

application = get_wsgi_application()
