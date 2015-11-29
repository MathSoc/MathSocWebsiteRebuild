# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0018_auto_20151128_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='has_key',
        ),
        migrations.AlterField(
            model_name='position',
            name='occupied_by',
            field=models.ManyToManyField(default=None, to='tangent.Member', blank=True),
        ),
    ]
