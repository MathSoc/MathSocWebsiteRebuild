# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0011_auto_20150713_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='action',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='order_key',
            field=models.IntegerField(default=99, unique=True),
            preserve_default=False,
        ),
    ]
