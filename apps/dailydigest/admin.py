# -*- encoding: utf-8 -*-

from django.contrib import admin

from apps.dailydigest.models import DailyIssue, InitialText


class InitialTextAdmin(admin.ModelAdmin):
    list_display = [
        'content',
        'is_active',
        'weight'
    ]

    list_filter = [
        'is_active',
        'weight'
    ]

    list_editable = [
        'is_active',
        'weight',
    ]


admin.site.register(DailyIssue)
admin.site.register(InitialText, InitialTextAdmin)
