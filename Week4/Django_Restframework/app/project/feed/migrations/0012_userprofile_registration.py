# Generated by Django 2.0.3 on 2018-03-26 08:38

from django.db import migrations, models
import project.feed.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0011_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='registration',
            field=models.CharField(default=project.feed.models.code_generator, max_length=15, unique=True,
                                   verbose_name='registration code'),
        ),
    ]