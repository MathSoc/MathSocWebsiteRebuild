# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0010_auto_20150201_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='location',
            field=models.CharField(default=b'Comfy Lounge', max_length=256),
            preserve_default=True,
        ),
    ]
