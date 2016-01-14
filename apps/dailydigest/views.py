import datetime

import requests
from django.shortcuts import render


def switch_section(old_name):
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

    return render(request, 'daily.html', {'items': result, 'date': date})


def daily(request, year, month, day):
    return base_daily(request, datetime.datetime(
            year=int(year), month=int(month), day=int(day)))


def daily_now(request):
    now = datetime.datetime.now()
    now -= datetime.timedelta(days=1)
    return base_daily(request, now)
