from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    progress = models.FloatField(verbose_name='Успеваемость', null=False, blank=False, default=0.0)
    birthday = models.DateField(verbose_name='Дата рождения', null=False, blank=False, editable=False)

    def __str__(self):
        return self.username

