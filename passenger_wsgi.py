import os
os.environ['MY_STATIC_ROOT'] = '/garethnums/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'garethnums.settings.prod'
import garethnames.wsgi
application = garethnames.wsgi.application
