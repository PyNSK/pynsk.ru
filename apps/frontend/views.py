# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView


class ThanksPage(TemplateView):
    template_name = 'pages/thanks.html'


class AboutPage(TemplateView):
    template_name = 'pages/about.html'


class IndexPage(TemplateView):
    template_name = 'home.html'
