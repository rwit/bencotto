import os.path
from settings_common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1') #Enable the debug context processor

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.dirname(__file__), 'sqlite.db'),
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    'default': {
#        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'djangotest',                      # Or path to database file if using sqlite3.
#        'USER': 'django',                      # Not used with sqlite3.
#        'PASSWORD': 'django',                  # Not used with sqlite3.
#        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'rusk',
    'south',
    'django_coverage', #enables to run "python manage.py test_coverage rusk -v2" for coverage information
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'rusk.context_processors.sidebar.sidebar',
    'rusk.context_processors.tabs.tabs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s - %(filename)s(%(lineno)d)',
        },
    },
    'handlers': {
        'file': {
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'level': 'DEBUG',
            'filename': os.path.join(os.path.dirname(__file__), 'logging', 'logging.log'),
            'maxBytes': 65536,
            'backupCount': 3,
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple',
            'level': 'ERROR',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rusk.context_processors.tabs': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'bencotto.rusk.image_processing.image_processing': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rusk.views': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

# django_coverage settings (overloading defaults from /usr/local/lib/python2.7/dist-packages/django_coverage/settings.py)
COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'reports')
