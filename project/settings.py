# Django settings for moscowdjango project.
import os

ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'components'))

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
TIME_ZONE = 'Asia/Novosibirsk'
LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_PATH, '../deploy/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, 'build'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
                'apps.meetup.context.menu',
                'apps.meetup.context.all_events_processor',

                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'zinnia.context_processors.version',  # Optional
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        }
    }
]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTHENTICATION_BACKENDS = (
    #    'admin_sso.auth.DjangoSSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = ('',)

INSTALLED_APPS = (
    'suit',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'djangobower',
    'storages',
    'pytils',
    'googlecharts',
    'sslserver',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',

    'apps.meetup',
    'apps.subscribers',
    'apps.frontend',
    'apps.tasks',

    # 'apps.articles',
)

# if DEBUG:
#    INSTALLED_APPS += ('debug_toolbar',)

ALLOWED_HOSTS = ['.project.ru', 'moscowdjango-staging.herokuapp.com', 'localhost', '.moscowpython.ru']

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
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

SERIALIZATION_MODULES = {
    'json-pretty': 'project.serializers.json_pretty',
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--failed', '--nologcapture']

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///{0}'.format(
            os.path.join(ROOT_PATH, 'project.db'))
    )
}

# security stuff
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECRET_KEY = 'pynsk'
ZINNIA_MARKUP_LANGUAGE = 'markdown'

BOWER_INSTALLED_APPS = (
    'jquery#2',
    'bootstrap#3.3.6',
    'bootstrap-material-design',
    'underscore',
)

try:
    from .local_settings import *
except ImportError as e:
    print(e)
