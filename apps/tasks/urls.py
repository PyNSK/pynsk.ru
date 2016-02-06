# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url, include

from apps.tasks.feeds import PublishedTasksFeed
from apps.tasks.views import TasksIndexPage, TaskPage

urlpatterns = patterns(
    '',
    url(r'^$', TasksIndexPage.as_view(), name='index'),
    url(r'(?P<pk>[-\w]+)/$', TaskPage.as_view(), name='task-detail'),
    url(r'rss/tasks', PublishedTasksFeed(), name='rss'),
    url(r'^search/', include('haystack.urls'), name='search'),

)
