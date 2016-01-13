import requests
from django.shortcuts import render


def switch_section(old_name):
    return {
        'Интересные проекты, инструменты, библиотеки': 'Библиотеки',
        'Новости': "Главные новости",
        'Конференции, события, встречи разработчиков': 'Встречи разработчиков',
        'Статьи': 'Статьи для прочтения за кружкой чая',
        'Видео': 'Видео достойные просмотра',
    }.get(old_name, old_name)


def daily(request):
    resp = requests.get('http://pythondigest.ru/api/items/2016/01/13/')
    # resp = requests.get('http://127.0.0.1:8000/api/items/2016/01/13/')
    items = []
    if resp and resp.json() and resp.json()['ok']:
        items = resp.json()['items']

    for item in items:
        item['section'] = switch_section(item['section__title'])
    return render(request, 'daily.html', {'items': items})
