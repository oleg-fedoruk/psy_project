from django.contrib.auth.models import User
from django.db import models


class SimpleTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='пользователь')
    title = models.CharField(verbose_name='название теста', max_length=512, null=False)
    start_at = models.DateTimeField(verbose_name='время начала прохождения', null=True, blank=True)
    finished_at = models.DateTimeField(verbose_name='время завершения прохождения', null=True, blank=True)

    def __str__(self):
        return self.title
