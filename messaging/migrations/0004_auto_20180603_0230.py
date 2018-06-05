# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-02 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_auto_20180603_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver_plate',
            field=models.CharField(default='', max_length=15),
        ),
    ]