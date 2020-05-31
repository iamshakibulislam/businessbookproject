# Generated by Django 3.0.5 on 2020-05-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200529_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='agent_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False, verbose_name='is_agent'),
        ),
    ]