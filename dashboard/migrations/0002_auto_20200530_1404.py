# Generated by Django 3.0.5 on 2020-05-30 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bought_adpack',
            name='buying_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 30, 14, 4, 56, 447615)),
        ),
    ]