# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-20 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='icon',
            field=models.ImageField(default='static/profilepics/pp.jpg', upload_to='static/profilepics', verbose_name='Group Photo'),
        ),
    ]
