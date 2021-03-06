"""
Cltlanglab Chat Server configuration file
"""
# chat_server.py
#!/usr/bin/env python
import os
import sys
from gevent import monkey
from socketio.server import SocketIOServer

# Need to add the project directory to the system path for this script.
from settings import base
sys.path.insert(0, os.path.abspath(str(base.PROJECT_DIR)))

import django
from django.core.wsgi import get_wsgi_application
from django.db import connections

# The setup command implicitly uses os.environ['DJANGO_SETTINGS_MODULE']
django.setup()
monkey.patch_all()
PORT = 8001

from django.conf import settings
host = settings.CHAT_SERVER_HOST

# Connect to django db
connections['default'].allow_thread_sharing = True

application = get_wsgi_application()

if __name__ == '__main__':
    print 'Listening on port  %s (no SSL)' % PORT
    SocketIOServer((host, PORT), application, resource="socket.io").serve_forever()

