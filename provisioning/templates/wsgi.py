"""
WSGI config for scoutproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import site

site.addsitedir('/vagrant/venv-server/serverproject/lib/python2.6/site-packages')
site.addsitedir('/vagrant/venv-server/serverproject')

from django.core.wsgi import get_wsgi_application
application = get_wsgi.application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scoutproject.settings")

application = get_wsgi_application()
