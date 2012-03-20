import sys, os

#Add the project-root to the path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'etc.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
