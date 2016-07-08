"""
WSGI config for chatroom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import site
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/cgi-bin/GLEAN')
sys.path.append('/var/www/cgi-bin/GLEAN/glean')
sys.path.append('/var/www/cgi-bin/GLEAN/glean/glean')
sys.path.append('/var/www/cgi-bin/GLEAN/glean/chat')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
