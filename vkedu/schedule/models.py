from django.db import models

# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(verbose_name='ФИО преподавателя', max_length=50, null=False)


class Lesson(models.Model):
    number_of_lesson = models.IntegerField(verbose_name='Номер вебинара', null=False)
    name_of_teacher = models.ManyToManyField(Teacher)
    time = models.DateTimeField(verbose_name='Дата и время проведения вебинара')
