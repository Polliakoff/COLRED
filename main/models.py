from asyncio.windows_events import NULL
from pickle import TRUE
from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


class Avatar_of_choice(models.Model):
    name = models.CharField('Название', max_length=50)
    usr = models.OneToOneField(User,on_delete=models.CASCADE,default='1',primary_key=True,related_name='chosen_avatar')

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    portrait = models.ImageField(upload_to ='user_images/')
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    xp = models.IntegerField(null=TRUE)
    background = models.CharField(max_length=100,null=TRUE)
    diety = models.CharField(max_length=100,null=TRUE)
    origin = models.CharField(max_length=100,null=TRUE)
    worldview = models.CharField(max_length=2,null=TRUE)
    attrib_strength = models.IntegerField(null=TRUE)
    attrib_agility = models.IntegerField(null=TRUE)
    attrib_charisma = models.IntegerField(null=TRUE)
    attrib_endurance = models.IntegerField(null=TRUE)
    attrib_intelligence = models.IntegerField(null=TRUE)
    armour_class = models.IntegerField(null=TRUE)
    hp = models.IntegerField(null=TRUE)
    speed = models.IntegerField(null=TRUE)
    skills_acrobatics = models.IntegerField(null=TRUE)
    skills_arcane = models.IntegerField(null=TRUE)
    skills_athletics = models.IntegerField(null=TRUE)
    skills_craft = models.IntegerField(null=TRUE)
    skills_decieve = models.IntegerField(null=TRUE)
    skills_diplomacy = models.IntegerField(null=TRUE)
    skills_intimidation = models.IntegerField(null=TRUE)
    skills_medicine = models.IntegerField(null=TRUE)
    skills_nature = models.IntegerField(null=TRUE)
    skills_occult = models.IntegerField(null=TRUE)
    skills_performance = models.IntegerField(null=TRUE)
    skills_religion = models.IntegerField(null=TRUE)
    skills_social = models.IntegerField(null=TRUE)
    skills_stealth = models.IntegerField(null=TRUE)
    skills_survival = models.IntegerField(null=TRUE)
    skills_theft = models.IntegerField(null=TRUE)
    save_resilience = models.IntegerField(null=TRUE)
    save_reflex = models.IntegerField(null=TRUE)
    save_resilience = models.IntegerField(null=TRUE)
    save_will = models.IntegerField(null=TRUE)
    weapon = models.CharField(max_length=100, null=TRUE) 
    attack = models.CharField(max_length=100, null=TRUE)
    damage = models.CharField(max_length=100, null=TRUE) 
    attention = models.IntegerField(null=TRUE)
    dc_class = models.IntegerField(null=TRUE)
    notes = models.TextField(null=TRUE)

    def __str__(self):
        return self.name

# Create your models here.
