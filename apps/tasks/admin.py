# -*- encoding: utf-8 -*-

from django.contrib import admin

from apps.tasks.models import Task, Tip


admin.site.register(Task)
admin.site.register(Tip)
