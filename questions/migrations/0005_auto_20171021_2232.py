# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20171021_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points_to', to='questions.Chapter'),
        ),
    ]
