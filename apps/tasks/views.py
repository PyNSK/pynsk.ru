# coding=utf-8
from django.views.generic import ListView, DetailView

from apps.tasks.models import Task


class TasksIndexPage(ListView):
    model = Task


class TaskPage(DetailView):
    model = Task
