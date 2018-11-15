
"""
    Base Django settings
    ====================
    For more information on this file, see https://docs.djangoproject.com/en/dev/topics/settings/
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/
"""

import json
import os
import pathlib

from django.core.exceptions import ImproperlyConfigured


# BASE DIRECTORIES
# ------------------------------------------------------------------------------

# PROJECT_PATH holds the path towards the root of the project.
# INSTALL_PATH holds the path towards the directory where the project's repository lives.
# By default INSTALL_PATH will correspond to the folder containing the project's repository (which
# should be compliant with the basic cases where the project is provisionned in a remote repository,
# a virtual machine or a container). But it should be noted that this path can be overriden by
# setting the DJANGO_INSTALL_PATH environment variable.

INSTALL_PATH = pathlib.Path(os.environ.get('DJANGO_INSTALL_PATH')) \
    if 'DJANGO_INSTALL_PATH' in os.environ else pathlib.Path(__file__).parents[1]
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# ENVIRONMENT SETTINGS HANDLING
# ------------------------------------------------------------------------------

# APP CONFIGURATION
# ------------------------------------------------------------------------------

INSTALLED_APPS = (
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django's admin app
    'django.contrib.admin',

    # Local apps
    'core',
)


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_DB', ''),
        'PORT': os.environ.get('DB_PORT', ''),
        'OPTIONS': os.environ.get('DB_OPTIONS', {}),
    },
}


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'EST'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


# See: https://docs.djangoproject.com/en/dev/ref/settings/#languages
LANGUAGES = (
    ('en', 'English'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = (
    #str(PROJECT_PATH / 'project' / 'locale'),
)


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.environ.get('SECRET_KEY')


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            os.path.join(PROJECT_PATH,  'templates'),
        ),
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                )),
            ]
        },
    },
]


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(INSTALL_PATH / 'static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
#STATICFILES_DIRS = (
    #
#)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-STATICFILES_STORAGE
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

iWEBPACK_LOADER = {
 #   'DEFAULT': {
  #      'STATS_FILE': str(PROJECT_PATH / 'demo/static/webpack-stats.json'),
   #     'BUNDLE_DIR_NAME': 'build/'
    #}
}


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
#MEDIA_ROOT = str(INSTALL_PATH / 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
#MEDIA_URL = '/media/'


# URL CONFIGURATION
# ------------------------------------------------------------------------------

ROOT_URLCONF = 'neuralresume.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
#WSGI_APPLICATION = 'wsgi.application'



# ADMIN CONFIGURATION
# ------------------------------------------------------------------------------

# URL of the admin page
ADMIN_URL = os.environ.get('ADMIN_URL')


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------

# See: http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
