# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-05 12:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parcelsapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('accepted', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelsapp.Parcels')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_of_parcel', to=settings.AUTH_USER_MODEL)),
                ('transporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporter_of_parcel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]