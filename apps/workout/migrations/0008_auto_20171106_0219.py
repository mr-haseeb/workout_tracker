# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0007_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='repetitions',
            field=models.DecimalField(decimal_places=1, max_digits=999),
        ),
    ]
