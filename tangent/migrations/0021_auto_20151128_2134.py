# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0020_auto_20151128_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='want_applications',
        ),
        migrations.AddField(
            model_name='position',
            name='want_applications',
            field=models.BooleanField(default=False),
        ),
    ]
