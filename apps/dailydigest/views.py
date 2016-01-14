import bisect
import datetime
import os
import random

import itertools
import requests
from django.conf import settings
from django.shortcuts import render
from apps.dailydigest.models import InitialText


def get_initial_text():
    weighted_choices = InitialText.objects.filter(is_active=True).values('content', weight)
    choices, weights = zip(*weighted_choices)
    cumdist = list(itertools.accumulate(weights))
    x = random.random() * cumdist[-1]
    return choices[bisect.bisect(cumdist, x)]

def get_initial_texts() -> list:
    with open(os.path.join(settings.ROOT_PATH, 'apps', "dailydigest", 'data', 'initial_texts.html')) as fio:
        return [x for x in fio.read().split('_+-SYMBOL-+_') if x]


def switch_section(old_name: str) -> str:
    return {
        'Интересные проекты, инструменты, библиотеки': 'Библиотеки',
        'Новости': "Главные новости",
        'Конференции, события, встречи разработчиков': 'Встречи разработчиков',
    }.get(old_name, old_name)


def base_daily(request, date):
    resp = requests.get('http://pythondigest.ru/api/items/{}/{}/{}/'.format(
            date.year,
            date.month,
            date.day
    ))
    # resp = requests.get('http://127.0.0.1:8000/api/items/2016/01/13/')
    items = []
    if resp and resp.json() and resp.json()['ok']:
        items = resp.json()['items']

    for item in items:
        item['section'] = switch_section(item['section__title'])

    result = {
        switch_section('Интересные проекты, инструменты, библиотеки'): [],
        switch_section('Новости'): [],
        switch_section('Конференции, события, встречи разработчиков'): [],
        switch_section('Статьи'): [],
        switch_section('Видео'): [],

    }
    for item in items:
        item['section'] = switch_section(item['section__title'])
        if item['section'] not in result:
            result[item['section']] = []
        result[item['section']].append(item)

        del item['section__title']

    return render(
            request, 'daily.html',
            {
                'items': result,
                'date': date,
                'initial_text': get_initial_text(),
            }
    )


def daily(request, year, month, day):
    return base_daily(request, datetime.datetime(
            year=int(year), month=int(month), day=int(day)))


def daily_now(request):
    now = datetime.datetime.now()
    now -= datetime.timedelta(days=1)
    return base_daily(request, now)
