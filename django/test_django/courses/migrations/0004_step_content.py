# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170209_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
