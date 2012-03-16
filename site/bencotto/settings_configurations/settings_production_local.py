import os.path
from settings_configurations.settings_common import *

DEBUG = False
TEMPLATE_DEBUG = False

#DEBUG = True
#TEMPLATE_DEBUG = DEBUG
#INTERNAL_IPS = ('127.0.0.1') #Enable the debug context processor

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://bencotto.local/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(SITE_ROOT, 'db', 'sqlite.db'),
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
    'apps.rusk',
    'south',
    #'django_coverage', #enables to run "python manage.py test_coverage rusk -v2" for coverage information
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    #'django.core.context_processors.request',
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
            'filename': os.path.join(SITE_ROOT, 'log', 'logging.log'),
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
        'rusk.image_processing.image_processing': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
