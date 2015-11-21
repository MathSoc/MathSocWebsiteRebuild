# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_bookingrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingrequest',
            name='status',
            field=models.IntegerField(default=1, verbose_name=((1, b'Requested'), (2, b'Accepted'), (3, b'Rejected'))),
        ),
    ]
