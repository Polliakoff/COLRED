from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Avatar_of_choice(models.Model):
    name = models.CharField('Название', max_length=50)
    usr = models.OneToOneField(User,on_delete=models.CASCADE,default='1',primary_key=True,related_name='chosen_avatar')

    def __str__(self):
        return self.name


# Create your models here.
