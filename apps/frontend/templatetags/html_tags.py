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
            'url': 'https://pythondigest.ru',
        },
        {
            'title': 'Дневной Python Дайджест',
            'description': 'Актуальные новости из мира Python за день',
            'url': reverse('dailydigest:index'),
        },
        {
            'title': 'Задачи',
            'description': 'Как же практика без теории? У нас свой сборник задач',
            'url': reverse('tasks:index'),
        },
        {
            'title': 'Встречи',
            'description': 'Мы регулярно проводим очные встречи',
            'url': reverse('meetup:index'),
        },
        {
            'title': 'Тесты',
            'description': 'Мы разработали тесты для проверки знаний',
            'url': 'https://tests.pynsk.ru',
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


class SetVarNode(template.Node):
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value

        return u""


@register.tag(name='set')
def set_var(parser, token):
    """
    {% set some_var = '123' %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form: {% set <var_name> = <var_value> %}")

    return SetVarNode(parts[1], parts[3])
