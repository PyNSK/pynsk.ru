# -*- encoding: utf-8 -*-

from django import template

register = template.Library()


@register.simple_tag()
def title_element():
    return "PyNSK - сайт о Python"


@register.assignment_tag
def bts_card_css():
    return ['info', 'default', 'primary', 'success', 'warning', 'danger']
