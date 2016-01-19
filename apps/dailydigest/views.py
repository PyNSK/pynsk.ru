import bisect
import datetime
import itertools
import random
import time

import requests
import vk
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from apps.dailydigest.models import InitialText, DailyIssue


def get_initial_text():
    weighted_choices = InitialText.objects.filter(is_active=True).values_list('content', 'weight')
    choices, weights = zip(*weighted_choices)
    cumdist = list(itertools.accumulate(weights))
    x = random.random() * cumdist[-1]
    return choices[bisect.bisect(cumdist, x)]


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


def post_to_wall(api, owner_id, message, **kwargs):
    data_dict = {
        'from_group': 1,
        'owner_id': owner_id,
        'message': message,
    }
    data_dict.update(**kwargs)
    return api.wall.post(**data_dict)


def publish_to_vk(content):
    app_id = settings.VK_APP_ID

    user_login = settings.VK_USER_LOGIN
    user_password = settings.VK_USER_PASSWORD
    session = vk.AuthSession(
            app_id=app_id,
            user_login=user_login,
            user_password=user_password,
            scope=','.join(['offline', 'wall'])
    )
    api = vk.API(session)
    attachment = 'photo-96469126_394565103'

    group_id = settings.VK_PYNSK_GROUP_ID
    group_to_id = settings.VK_PYTHON_PROGRAMMING_ID
    # dat = datetime.datetime.today()
    # dat.replace(hour=15, minute=0)
    result = post_to_wall(api, group_id, content, **{'attachments': attachment})

    if 'post_id' in result:
        time.sleep(1)
        api.wall.repost(
                object='wall{}_{}'.format(group_id, result['post_id']),
                group_id=abs(int(group_to_id)),

        )


def daily_create(request):
    if request.method == 'GET':
        publish_to_vk(request.GET.get('content'))
        DailyIssue(
                title=request.GET.get('title'),
                description=request.GET.get('content'),
                status='active',
                published_at=datetime.datetime.strptime(request.GET.get('date'), '%d.%m.%Y'),
        ).save()
        return HttpResponse('Ok')
    else:
        return HttpResponse('Error')
