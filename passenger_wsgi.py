import os
os.environ['MY_STATIC_ROOT'] = '/nums/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'garethnums.settings.prod'
os.environ['DJANGO_LOG_DIR'] = '/var/nlm/logs/django';
import garethnums.wsgi
application = garethnums.wsgi.application
