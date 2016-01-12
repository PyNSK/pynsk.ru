# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='categories',
        ),
    ]
