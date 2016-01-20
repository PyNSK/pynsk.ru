# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url

from apps.dailydigest.views import daily, daily_now, daily_create, DailyDigestIndexPage, DailyDigestPage

urlpatterns = patterns(
        '',
        url('^create$', daily_now, name='now'),
        url('^create/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)$', daily, name='daily'),
        url('^ajax/create$', daily_create, name='create'),
        url(r'^$', DailyDigestIndexPage.as_view(), name='index'),
        url(r'(?P<pk>[-\w]+)/$', DailyDigestPage.as_view(), name='dailydigest-detail'),
)
