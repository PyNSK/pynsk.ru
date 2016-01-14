# -*- encoding: utf-8 -*-

from django.contrib import admin

from apps.dailydigest.models import DailyIssue, InitialText

admin.site.register(DailyIssue)
admin.site.register(InitialText)
