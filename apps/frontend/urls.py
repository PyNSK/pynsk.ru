# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url, include
from .views import IndexPage


urlpatterns = patterns('',
    url('^$', IndexPage.as_view(), name='index'),
)
