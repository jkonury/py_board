import os
import sys
import site

site.addsitedir('/home/hong/virtualEnvs/board/lib/python3.4/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'py_board.settings'

sys.path.insert(0, '/home/hong/dev/pycharm/python3/django/py_board')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()