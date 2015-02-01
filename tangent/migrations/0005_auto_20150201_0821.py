# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0004_auto_20150201_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='positions',
        ),
        migrations.AddField(
            model_name='position',
            name='is_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='position',
            name='organization',
            field=models.ForeignKey(default=0, to='tangent.Organization'),
            preserve_default=False,
        ),
    ]
