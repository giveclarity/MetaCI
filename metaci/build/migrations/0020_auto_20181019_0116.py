# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-19 01:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0019_build_planrepo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='build',
            options={'ordering': ['-time_queue'], 'permissions': (('search_builds', 'Search Builds'),)},
        ),
    ]