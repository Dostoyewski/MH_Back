# Generated by Django 2.2.1 on 2020-04-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200404_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='army_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='hero',
            name='army_name_short',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='hero',
            name='father_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='hero',
            name='info',
            field=models.CharField(default='Нет информации', max_length=1000),
        ),
        migrations.AddField(
            model_name='hero',
            name='path',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
