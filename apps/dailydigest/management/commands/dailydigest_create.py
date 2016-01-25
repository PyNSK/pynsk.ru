# -*- encoding: utf-8 -*-
import datetime

from django.core.management.base import BaseCommand
from django.template import loader, Context, Template

from apps.dailydigest.models import DailyIssue
from apps.dailydigest.views import get_digest_data, publish_to_vk


def main():
    now = datetime.datetime.now()
    now -= datetime.timedelta(days=1)

    t = loader.get_template('include/dailyissue_content.html')
    c = Context(get_digest_data(now))
    content = t.render(c)

    # name_template = Template('Дневной дайджест: {{ date|date:"d.m.Y" }}')
    date_str = now.strftime('%d.%m.%Y')
    # title = name_template.render(Context({'date': now}))
    title = "Дневной дайджест: {}".format(date_str)

    DailyIssue(
            title=title,
            description=content,
            status='active',
            published_at=now,
    ).save()
    publish_to_vk(content)


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
