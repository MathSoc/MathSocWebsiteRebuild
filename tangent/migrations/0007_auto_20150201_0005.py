# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0006_auto_20150201_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='affiliations',
            field=models.CharField(max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
