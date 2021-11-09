from django.db import models

# Create your models here.


class Teacher(models.Model):
    FullName = models.CharField(verbose_name='ФИО преподавателя', max_length=50, null=False)


class Lesson(models.Model):
    NumberOfLesson = models.IntegerField(verbose_name='Номер вебинара', null=False)
    NameOfTeacher = models.ManyToManyField(Teacher)
    Time = models.DateTimeField(verbose_name='Дата и время проведения вебинара')
