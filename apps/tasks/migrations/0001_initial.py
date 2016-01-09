# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import tagging.fields
import zinnia.models_bases.entry


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0002_lead_paragraph_and_image_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('lead', models.TextField(verbose_name='lead', help_text='Lead paragraph', blank=True)),
                ('excerpt', models.TextField(verbose_name='excerpt', help_text='Used for SEO purposes.', blank=True)),
                ('image', models.ImageField(verbose_name='image', upload_to=zinnia.models_bases.entry.image_upload_to_dispatcher, blank=True, help_text='Used for illustration.')),
                ('image_caption', models.TextField(verbose_name='caption', help_text="Image's caption.", blank=True)),
                ('featured', models.BooleanField(verbose_name='featured', default=False)),
                ('tags', tagging.fields.TagField(verbose_name='tags', max_length=255, blank=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('slug', models.SlugField(verbose_name='slug', unique_for_date='creation_date', help_text="Used to build the entry's URL.", max_length=255)),
                ('status', models.IntegerField(verbose_name='status', choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')], default=0, db_index=True)),
                ('creation_date', models.DateTimeField(verbose_name='creation date', help_text="Used to build the entry's URL.", default=django.utils.timezone.now, db_index=True)),
                ('last_update', models.DateTimeField(verbose_name='last update', default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(verbose_name='categories', related_name='tasks_task_related', blank=True, to='zinnia.Category')),
                ('related', models.ManyToManyField(verbose_name='related entries', related_name='_task_related_+', blank=True, to='tasks.Task')),
            ],
            options={
                'verbose_name': 'task',
                'ordering': ['-creation_date'],
                'get_latest_by': 'creation_date',
                'verbose_name_plural': 'tasks',
                'permissions': (('can_view_all', 'Can view all entries'), ('can_change_status', 'Can change status'), ('can_change_author', 'Can change author(s)')),
            },
        ),
        migrations.AlterIndexTogether(
            name='task',
            index_together=set([('slug', 'creation_date'), ('status', 'creation_date')]),
        ),
    ]
