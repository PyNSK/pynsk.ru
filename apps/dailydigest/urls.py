# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url

from apps.dailydigest.views import daily

urlpatterns = patterns(
        '',
        url('^$', daily, name='index'),

)
