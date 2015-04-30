# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0007_auto_20150201_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cover_letter',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
