# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0003_position_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
