# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locker',
            name='empty',
        ),
        migrations.RemoveField(
            model_name='locker',
            name='id',
        ),
        migrations.AlterField(
            model_name='locker',
            name='locker_number',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='locker',
            name='owner',
            field=models.ForeignKey(blank=True, to='tangent.Member', null=True),
            preserve_default=True,
        ),
    ]
