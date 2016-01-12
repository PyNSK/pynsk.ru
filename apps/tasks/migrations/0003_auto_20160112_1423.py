# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('status', models.IntegerField(verbose_name='status', choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')], db_index=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'task', 'permissions': (('can_view_all', 'Can view all entries'), ('can_change_status', 'Can change status'), ('can_change_author', 'Can change author(s)')), 'verbose_name_plural': 'tasks', 'get_latest_by': 'creation_date', 'ordering': ['-number', '-creation_date']},
        ),
        migrations.AddField(
            model_name='tip',
            name='task',
            field=models.ForeignKey(to='tasks.Task'),
        ),
    ]
