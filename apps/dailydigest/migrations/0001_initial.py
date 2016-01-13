# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyIssue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(null=True, blank=True, verbose_name='Описание')),
                ('image', models.ImageField(null=True, upload_to='issues', blank=True, verbose_name='Постер')),
                ('published_at', models.DateField(null=True, blank=True, verbose_name='Дата публикации')),
                ('status', models.CharField(max_length=10, verbose_name='Статус', choices=[('active', 'Активный'), ('draft', 'Черновик')], default='draft')),
            ],
            options={
                'verbose_name_plural': 'Выпуски дневного дайджеста',
                'verbose_name': 'Выпуск дневного дайджеста',
                'ordering': ['-pk'],
            },
        ),
    ]
