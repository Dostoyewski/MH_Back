# Generated by Django 2.2.1 on 2020-04-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200404_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='info',
            field=models.TextField(default='Нет информации', max_length=1000),
        ),
        migrations.AlterField(
            model_name='hero',
            name='path',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]