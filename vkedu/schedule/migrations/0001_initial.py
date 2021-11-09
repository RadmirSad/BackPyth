# Generated by Django 3.2.9 on 2021-11-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50, verbose_name='ФИО преподавателя')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumberOfLesson', models.IntegerField(verbose_name='Номер вебинара')),
                ('Time', models.DateTimeField(verbose_name='Дата и время проведения вебинара')),
                ('NameOfTeacher', models.ManyToManyField(to='schedule.Teacher')),
            ],
        ),
    ]