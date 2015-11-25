from datetime import datetime
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)

    created_on = models.DateTimeField(default=datetime.max, editable=False)
    is_published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True)
    comments_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.title
