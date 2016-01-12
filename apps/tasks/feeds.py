# -*- encoding: utf-8 -*-

from django.contrib.syndication.views import Feed
from zinnia.managers import PUBLISHED

from apps.tasks.models import Task


class TasksFeed(Feed):
    title = u"PyNSK - сайт о Python Задачи"
    link = '/'
    description = u"""Сборник практических задач по программированию."""

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.rss_content

    def item_link(self, item):
        return item.link

    def item_pubdate(self, item):
        return item.last_update or item.creation_date


class PublishedTasksFeed(TasksFeed):
    @staticmethod
    def items():
        return Task.objects.filter(
                status=PUBLISHED,
        ).order_by('-creation_date')[:20]
