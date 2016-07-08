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

# python virtualenv dir
site.addsitedir("/var/www/cgi-bin/virtualenv/lib/python3.4/site-packages")

sys.path.append('/var/www/cgi-bin/GLEAN')
sys.path.append('/var/www/cgi-bin/GLEAN/glean')
sys.path.append('/var/www/cgi-bin/GLEAN/glean/glean')
sys.path.append('/var/www/cgi-bin/GLEAN/glean/chat')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

activate_env = os.path.expanduser("/var/www/cgi-bin/virtualenv/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))
'''
with open(activate_env) as f:
    code = compile(f.read(), activate_env, 'exec')
    exec(code, dict(__file__=activate_env))
'''

exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), dict(__file__=activate_env))

application = get_wsgi_application()
