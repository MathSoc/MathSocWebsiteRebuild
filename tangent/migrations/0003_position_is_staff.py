# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0002_auto_20170223_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
