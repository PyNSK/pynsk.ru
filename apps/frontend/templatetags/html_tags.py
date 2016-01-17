# -*- encoding: utf-8 -*-

import re

import pygments
from django import template
from django.core.urlresolvers import reverse
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.python import PythonLexer

register = template.Library()


@register.simple_tag()
def title_element():
    return "PyNSK - сайт о Python"


@register.assignment_tag
def bts_card_css():
    return ['info', 'primary', 'success', 'warning', 'danger']


@register.assignment_tag
def projects():
    return [
        {
            'title': 'Статьи',
            'description': 'Мы пишем много текстового контента',
            'url': '/blog',
        },
        {
            'title': 'Недельный Python Дайджест',
            'description': 'Собираем актуальные новости из мира Python',
            'url': 'http://pythondigest.ru',
        },
        {
            'title': 'Задачи',
            'description': 'Как же практика без теории? У нас свой сборник задач',
            'url': reverse('tasks:index'),
        },
    ]


regex = re.compile(r'<code>(.*?)</code>', re.DOTALL)


@register.filter(name='pygment')
def pygment(value):
    try:
        last_end = 0
        to_return = ''
        found = 0
        for match_obj in regex.finditer(value):
            code_string = match_obj.group(1)
            try:
                lexer = pygments.lexers.guess_lexer(code_string)
            except ValueError:
                lexer = PythonLexer()
            pygmented_string = pygments.highlight(code_string, lexer, HtmlFormatter())
            to_return = to_return + value[last_end:match_obj.start(1)] + pygmented_string
            last_end = match_obj.end(1)
            found += + 1
        to_return = to_return + value[last_end:]
        return to_return
    except:
        return value
