# Generated by Django 3.0.7 on 2020-07-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.TextField(default=''),
        ),
    ]
