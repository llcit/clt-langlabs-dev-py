# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-07 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0002_auto_20161205_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpageactivity',
            name='attachments',
        ),
    ]
