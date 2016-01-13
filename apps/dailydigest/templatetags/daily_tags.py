# -*- encoding: utf-8 -*-

from django import template

register = template.Library()


@register.simple_tag()
def crete_hr_line(string, symbol='-'):
    return symbol * len(string)
