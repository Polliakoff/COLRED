from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Avatar_of_choice(models.Model):
    name = models.CharField('Название', max_length=50)
    #usr = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default='blank')

    def __str__(self):
        return self.name


# Create your models here.
