# Generated by Django 3.0.7 on 2020-06-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200627_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl2',
            field=models.TextField(default=''),
        ),
    ]