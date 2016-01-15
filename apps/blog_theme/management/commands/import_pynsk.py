# -*- encoding: utf-8 -*-
import datetime
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from mezzanine.generic.models import AssignedKeyword, Keyword
from transliterate import slugify, translit
from transliterate.exceptions import LanguageDetectionError


def parse():
    folder = '/home/warmonger/Develop/Groups/PyNSK/pynsk/content/article/'

    _files = []
    for dir, _, files in os.walk(folder):
        _files.extend([os.path.join(dir, x) for x in files if x and x.endswith('.md')])

    categories = []
    for x in _files:
        with open(x, 'r') as fio:
            head = [next(fio) for _ in range(4)]

            space = next(fio).strip()
            while not space:
                space = next(fio)

            categories.append(head[3].replace('Category: ', '').replace('-', ' ').replace(' ', ' ').strip())

    categories = list(set(categories))

    for x in categories:
        try:
            if not x:
                continue
            slug = translit(x.strip(), reversed=True).replace(' ', '-').lower()
            BlogCategory.objects.get_or_create(title=x, slug=slug)
        except LanguageDetectionError as e:
            print(e, x)

    for x in _files:
        with open(x, 'r') as fio:
            head = [next(fio) for _ in range(4)]

            space = next(fio).strip()
            while not space:
                space = next(fio)

            raw_title = head[0].replace('Title: ', '').strip()

            slug = slugify(raw_title)

            date = datetime.datetime.strptime(
                    head[1].replace('Date: ', '').strip(), "%Y-%m-%d %H:%M")
            tags = [x.strip() for x in head[2].replace('Tags: ', '').strip().split(',') if x and x.strip()]

            category = head[3].replace('Category: ', '').replace('-', ' ').replace(' ', ' ').strip()
            text = fio.read().replace('!embedlycard', '!embed')

            post, created = BlogPost.objects.get_or_create(
                    title=raw_title,
                    slug=slug,
                    publish_date=date,
                    status=CONTENT_STATUS_PUBLISHED,
                    user=User.objects.get(username='admin'),
                    content=text,
            )

            for tag in tags:
                keyword, _ = Keyword.objects.get_or_create(title=tag)
                post.keywords.add(AssignedKeyword(keyword=keyword))

            post.categories.add(BlogCategory.objects.get_or_create(title=category)[0])


class Command(BaseCommand):
    def handle(self, *args, **options):
        parse()
