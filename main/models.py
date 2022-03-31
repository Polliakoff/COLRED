from asyncio.windows_events import NULL
from pickle import TRUE
from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from string import Template
from django.utils.safestring import mark_safe

class Avatar_of_choice(models.Model):
    name = models.CharField('Название', max_length=50)
    usr = models.OneToOneField(User,on_delete=models.CASCADE,default='1',primary_key=True,related_name='chosen_avatar')

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    portrait = models.ImageField(upload_to ='user_images/',blank = True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    chr_class = models.CharField(max_length=13,null=TRUE,blank=TRUE)
    xp = models.IntegerField(null=TRUE,blank=TRUE)
    background = models.CharField(max_length=100,null=TRUE,blank=TRUE)
    diety = models.CharField(max_length=100,null=TRUE,blank=TRUE)
    origin = models.CharField(max_length=100,null=TRUE,blank=TRUE)
    worldview = models.CharField(max_length=2,null=TRUE,blank=TRUE)
    attrib_strength = models.IntegerField(null=TRUE,blank=TRUE)
    attrib_agility = models.IntegerField(null=TRUE,blank=TRUE)
    attrib_charisma = models.IntegerField(null=TRUE,blank=TRUE)
    attrib_endurance = models.IntegerField(null=TRUE,blank=TRUE)
    attrib_intelligence = models.IntegerField(null=TRUE,blank=TRUE)
    attrib_wisdom = models.IntegerField(null=TRUE,blank=TRUE)
    armour_class = models.IntegerField(null=TRUE,blank=TRUE)
    hp = models.IntegerField(null=TRUE,blank=TRUE)
    speed = models.IntegerField(null=TRUE,blank=TRUE)
    skills_acrobatics = models.IntegerField(null=TRUE,blank=TRUE)
    skills_arcane = models.IntegerField(null=TRUE,blank=TRUE)
    skills_athletics = models.IntegerField(null=TRUE,blank=TRUE)
    skills_craft = models.IntegerField(null=TRUE,blank=TRUE)
    skills_decieve = models.IntegerField(null=TRUE,blank=TRUE)
    skills_diplomacy = models.IntegerField(null=TRUE,blank=TRUE)
    skills_intimidation = models.IntegerField(null=TRUE,blank=TRUE)
    skills_medicine = models.IntegerField(null=TRUE,blank=TRUE)
    skills_nature = models.IntegerField(null=TRUE,blank=TRUE)
    skills_occult = models.IntegerField(null=TRUE,blank=TRUE)
    skills_performance = models.IntegerField(null=TRUE,blank=TRUE)
    skills_religion = models.IntegerField(null=TRUE,blank=TRUE)
    skills_social = models.IntegerField(null=TRUE,blank=TRUE)
    skills_stealth = models.IntegerField(null=TRUE,blank=TRUE)
    skills_survival = models.IntegerField(null=TRUE,blank=TRUE)
    skills_theft = models.IntegerField(null=TRUE,blank=TRUE)
    save_resilience = models.IntegerField(null=TRUE,blank=TRUE)
    save_reflex = models.IntegerField(null=TRUE,blank=TRUE)
    save_resilience = models.IntegerField(null=TRUE,blank=TRUE)
    save_will = models.IntegerField(null=TRUE,blank=TRUE)
    weapon = models.CharField(max_length=100, null=TRUE,blank=TRUE) 
    attack = models.CharField(max_length=100, null=TRUE,blank=TRUE)
    damage = models.CharField(max_length=100, null=TRUE,blank=TRUE) 
    attention = models.IntegerField(null=TRUE,blank=TRUE)
    dc_class = models.IntegerField(null=TRUE,blank=TRUE)
    notes = models.TextField(null=TRUE,blank=TRUE)

    def __str__(self):
        return self.name

# Create your models here.
