from dataclasses import fields
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.forms import ModelForm
from .models import Character
from django.forms import NumberInput, TextInput, Textarea

class psw_ch(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(psw_ch, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None

class Great_List_Form(ModelForm):
    class Meta:
        model = Character
        fields = [
            'attrib_strength',
            'attrib_agility',
            'attrib_charisma',
            'attrib_endurance',
            'attrib_intelligence',
            'attrib_wisdom',
        ]
        widgets = {
            'attrib_strength': NumberInput(attrs={
                'id' : 'STR',
            }),
            'attrib_agility': NumberInput(attrs={
                'id' : 'DX',
            }),
            'attrib_charisma': NumberInput(attrs={
                'id' : 'CHR',
            }),
            'attrib_endurance': NumberInput(attrs={
                'id' : 'CON',
            }),
            'attrib_intelligence': NumberInput(attrs={
                'id' : 'IN',
            }),
        }