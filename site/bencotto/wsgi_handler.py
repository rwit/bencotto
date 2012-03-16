import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)
sys.path.append(path + '/..')
    
os.environ['DJANGO_SETTINGS_MODULE'] = 'bencotto.settings_production'
#os.environ['DJANGO_SETTINGS_MODULE'] = 'bencotto.settings_development'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
