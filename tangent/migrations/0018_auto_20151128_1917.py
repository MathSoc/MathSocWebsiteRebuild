# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0017_auto_20151128_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='position',
            name='start_date',
        ),
    ]
