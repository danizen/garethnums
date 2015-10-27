"""
Django settings for garethnums project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'un3s-zaz*1h9p%!!-hcri*mxktywb9-llj$o)z%_#a^c87m5d9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = ( 'templates', )

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'garethnums',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'garethnums.urls'

WSGI_APPLICATION = 'garethnums.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )

STATIC_ROOT = os.path.join(BASE_DIR, 'public')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

urlprefix = os.environ.setdefault('MY_URL_ROOT', '')
staticprefix = os.environ.setdefault('MY_STATIC_ROOT', '/{}static/'.format(urlprefix))
STATIC_URL = staticprefix

logdir = os.environ.setdefault('DJANGO_LOG_DIR', os.path.join(BASE_DIR, "logs"))
if not os.path.exists(logdir):
    os.mkdir(logdir)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'full': {
            'format': '[%(asctime)s] %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'formatter': 'full',
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'encoding': 'UTF-8',
            'when': 'H',
            'interval': 1,
            'filename': os.path.join(logdir, 'garethnums.log'),
        },
        'console': {
            'formatter': 'full',
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propogate': True,
        },
    },
}
