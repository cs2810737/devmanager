# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_developer_hours_worked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='current_project',
            new_name='project',
        ),
    ]
