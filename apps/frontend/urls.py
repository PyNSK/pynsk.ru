# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url

from apps.frontend.views import ThanksPage, AboutPage

urlpatterns = patterns(
        '',
        url(r'^thanks$', ThanksPage.as_view(), name='thanks'),
        url(r'^about$', AboutPage.as_view(), name='about'),

)
