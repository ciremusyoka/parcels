# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-01 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagerapp', '0005_auto_20180501_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_address',
        ),
    ]