# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20161012_0737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['-name']},
        ),
    ]
