# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20171021_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=400),
        ),
    ]
