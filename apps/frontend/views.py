# coding=utf-8

from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = 'index.html'
    # context_object_name = 'events'
    #
    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         qs = Event.objects.all()
    #     else:
    #         qs = Event.archived.all()
    #
    #     return qs.prefetch_related('talks', 'talks__speaker', 'talks__event')[:3]
    #
    # def get_context_data(self, **kwargs):
    #     context = super(IndexPage, self).get_context_data(**kwargs)
    #
    #     # TODO: choose how select people for index page
    #     # I see two options:
    #     # By last talks -  Speaker.objects.order_by("-talks__event__id", "talk__position")[:9]
    #     # Random: Speaker.objects.order_by("?")[:9]
    #
    #     context.update({
    #         'speakers': Speaker.objects.order_by("?")[:10],
    #         'main_event': Event.spotlight(self.request.user.is_staff),
    #         'show_more_link': True,
    #         'can_vote': can_vote(self.request)
    #     })
    #     return context
