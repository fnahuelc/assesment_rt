# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managerApp', '0029_auto_20170417_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mluser',
            name='access_token',
            field=models.CharField(default='No acces token', max_length=200),
        ),
    ]
