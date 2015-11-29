# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0016_auto_20151128_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(to='tangent.Member', blank=True),
        ),
    ]
