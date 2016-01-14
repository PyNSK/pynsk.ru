from django.db import models

ISSUE_STATUS_CHOICES = (('active', u'Активный'), ('draft', u'Черновик'),)


class DailyIssue(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок', )
    description = models.TextField(verbose_name=u'Описание',
                                   null=True,
                                   blank=True, )
    image = models.ImageField(verbose_name=u'Постер',
                              upload_to='issues',
                              null=True,
                              blank=True, )
    published_at = models.DateField(verbose_name=u'Дата публикации',
                                    null=True,
                                    blank=True, )
    status = models.CharField(verbose_name=u'Статус',
                              max_length=10,
                              choices=ISSUE_STATUS_CHOICES,
                              default='draft', )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']
        verbose_name = u'Выпуск дневного дайджеста'
        verbose_name_plural = u'Выпуски дневного дайджеста'


class InitialText(models.Model):
    content = models.TextField(verbose_name='Текст')
    weight = models.PositiveIntegerField(default=100, verbose_name='Вес')
    is_active = models.BooleanField(verbose_name='Активна', default=True, )

    def __str__(self):
        return self.content[:50]

    class Meta:
        ordering = ['is_active', 'weight', '-pk']
        verbose_name = u'Вводный текст дневного дайджеста'
        verbose_name_plural = u'Вводные тексты дневного дайджеста'
