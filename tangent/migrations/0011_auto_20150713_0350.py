# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0010_auto_20150713_0333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='organization',
        ),
        migrations.AddField(
            model_name='organization',
            name='positions',
            field=models.ManyToManyField(to='tangent.Position'),
        ),
    ]
