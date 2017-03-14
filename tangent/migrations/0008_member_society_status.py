# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0007_auto_20170223_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='society_status',
            field=models.IntegerField(default=1, choices=[(1, 'Have not cached answer'), (2, 'Society Member'), (3, 'Not Society Member')]),
        ),
    ]
