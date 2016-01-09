from django.contrib import admin

from apps.tasks.models import Task


class TasksAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task)
