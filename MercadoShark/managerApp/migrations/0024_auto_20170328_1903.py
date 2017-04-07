# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 19:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managerApp', '0023_remove_article_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('category_id', models.CharField(max_length=60)),
                ('price', models.FloatField(default='10')),
                ('currency_id', models.CharField(max_length=60)),
                ('available_quantity', models.IntegerField(default='1')),
                ('buying_mode', models.CharField(max_length=60)),
                ('listing_type_id', models.CharField(max_length=60)),
                ('condition', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=9999)),
                ('video_id', models.CharField(max_length=60)),
                ('warranty', models.CharField(max_length=60)),
                ('pictures', models.URLField(max_length=2000)),
                ('itemId', models.CharField(max_length=60)),
                ('permalink', models.URLField(max_length=2000)),
                ('account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='managerApp.MlUser')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='account',
        ),
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]