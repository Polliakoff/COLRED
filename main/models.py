from statistics import mode
from django.db import models

class User(models.Model):
    login = models.CharField('Логин', max_length=20)
    password = models.CharField('Пароль',max_length=100)

    def __str__(self):
        return self.login



# Create your models here.
