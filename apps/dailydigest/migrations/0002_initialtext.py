# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailydigest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('content', models.TextField(verbose_name='Текст')),
                ('weight', models.PositiveIntegerField(verbose_name='Вес', default=100)),
                ('is_active', models.BooleanField(verbose_name='Активна', default=True)),
            ],
            options={
                'verbose_name': 'Вводный текст дневного дайджеста',
                'verbose_name_plural': 'Вводные тексты дневного дайджеста',
                'ordering': ['is_active', 'weight', '-pk'],
            },
        ),
    ]
