# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20170510_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp', 'content']},
        ),
    ]
