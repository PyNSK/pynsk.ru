# coding=utf-8
from django.views.generic import ListView

from apps.tasks.models import Task


class TasksIndexPage(ListView):
    model = Task
