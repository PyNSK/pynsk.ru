# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url

from apps.dailydigest.views import daily, daily_now, daily_create

urlpatterns = patterns(
        '',
        url('^$', daily_now, name='index'),
        url('^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)$', daily, name='daily'),
        url('^create$', daily_create, name='create')

)
