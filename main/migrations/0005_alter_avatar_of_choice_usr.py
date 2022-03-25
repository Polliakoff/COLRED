# Generated by Django 4.0.3 on 2022-03-25 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_avatar_of_choice_usr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar_of_choice',
            name='usr',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='avatarochka', to=settings.AUTH_USER_MODEL),
        ),
    ]
