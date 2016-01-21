# -*- encoding: utf-8 -*-

from haystack import indexes
from zinnia.managers import PUBLISHED

from apps.tasks.models import Task


class TaskIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content = indexes.CharField(model_attr='content')
    title = indexes.CharField(model_attr='title')
    tags = indexes.CharField(model_attr='tags')
    status = indexes.IntegerField(model_attr='status')

    def get_model(self):
        return Task

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(status=PUBLISHED)
