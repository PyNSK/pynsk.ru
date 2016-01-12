# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20160112_1423'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='task',
            index_together=set([('creation_date',), ('status', 'creation_date')]),
        ),
        migrations.RemoveField(
            model_name='task',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='task',
            name='lead',
        ),
        migrations.RemoveField(
            model_name='task',
            name='related',
        ),
        migrations.RemoveField(
            model_name='task',
            name='slug',
        ),
    ]
