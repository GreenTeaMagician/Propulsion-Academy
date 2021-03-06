# Generated by Django 2.0.3 on 2018-03-22 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_dislike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followees',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL,
                                         verbose_name='following'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile',
                                       to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
