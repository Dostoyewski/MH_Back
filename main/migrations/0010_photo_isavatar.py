# Generated by Django 2.2.1 on 2020-04-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_hero_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='isAvatar',
            field=models.BooleanField(default=False),
        ),
    ]
