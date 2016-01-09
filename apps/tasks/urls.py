# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url, include
from apps.tasks.views import TasksIndexPage


urlpatterns = patterns('',
    url('^$', TasksIndexPage.as_view(), name='index'),
)
