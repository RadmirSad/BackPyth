# Generated by Django 3.2.9 on 2021-11-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameOfProgram', models.CharField(max_length=30, verbose_name='Название курса')),
                ('Lessons', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.lesson', verbose_name='Список вебинаров')),
            ],
        ),
    ]
