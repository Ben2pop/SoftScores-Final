# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 08:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20180318_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demoproject',
            name='project_hr_admin',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]