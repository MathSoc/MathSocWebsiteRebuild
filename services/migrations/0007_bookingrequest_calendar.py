# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20150910_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingrequest',
            name='calendar',
            field=models.CharField(default='cnd', max_length=256),
            preserve_default=False,
        ),
    ]
