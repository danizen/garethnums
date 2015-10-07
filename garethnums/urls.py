import os
from django.conf.urls import patterns, include, url

prefix = os.environ.setdefault('MY_URL_ROOT', '')

urlpatterns = patterns('',
    url(r'^{}$'.format(prefix), 'garethnums.views.numbers'),
)
