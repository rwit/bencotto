import sys
import os

#Add the project-root to the path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_configurations.settings_production_local'
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_configurations.settings_development'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
