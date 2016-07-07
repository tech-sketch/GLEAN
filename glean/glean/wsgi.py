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

# python仮想環境のインストール済みパッケージディレクトリ
site.addsitedir("/home/glean/virtualenv/lib/python3.4/ste-packages")

sys.path.append('/home/glean/git-repos/GLEAN')
sys.path.append('/home/glean/git-repos/GLEAN/glean')
sys.path.append('/home/glean/git-repos/GLEAN/glean/glean')
sys.path.append('/home/glean/git-repos/GLEAN/glean/chat')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "glean.settings")

# 仮想環境の実行パス
activate_env = os.path.expanduser("/home/glean/virtualenv/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))
'''
with open(activate_env) as f:
    code = compile(f.read(), activate_env, 'exec')
    exec(code, dict(__file__=activate_env))
'''

exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), dict(__file__=activate_env))

application = get_wsgi_application()
