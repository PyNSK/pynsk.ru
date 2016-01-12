# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url

from apps.tasks.feeds import PublishedTasksFeed
from apps.tasks.views import TasksIndexPage, TaskPage

urlpatterns = patterns(
        '',
        url('^$', TasksIndexPage.as_view(), name='index'),
        url(r'^task/(?P<pk>[-\w]+)/$', TaskPage.as_view(), name='task-detail'),
        url('rss/tasks', PublishedTasksFeed(), name='rss'),

)
