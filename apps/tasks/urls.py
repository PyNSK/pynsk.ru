# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url, include
from apps.tasks.views import TasksIndexPage, TaskPage


urlpatterns = patterns('',
    url('^$', TasksIndexPage.as_view(), name='index'),
    url(r'^task/(?P<pk>[-\w]+)/$', TaskPage.as_view(), name='task-detail'),
)
