from django.db import models
from schedule.models import Lesson

# Create your models here.


class Program(models.Model):
    name = models.CharField(verbose_name='Название курса', max_length=30, null=False)
    lessons = models.ForeignKey(Lesson, verbose_name='Список вебинаров', blank=False,
                                null=False, on_delete=models.PROTECT)

