# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 14:24
from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import django.db.models.deletion
from django.db import migrations, models
from future import standard_library

standard_library.install_aliases()


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_polymorphic_answers_to_kiss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='questions', to='survey.Category'
            ),
        ),
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='questions', to='survey.Survey'
            ),
        ),
    ]
