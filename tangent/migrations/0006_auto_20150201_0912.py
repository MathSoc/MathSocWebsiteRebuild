# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0005_auto_20150201_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='meetings',
        ),
        migrations.AddField(
            model_name='meeting',
            name='organization',
            field=models.ForeignKey(default=0, to='tangent.Organization'),
            preserve_default=False,
        ),
    ]
