# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0005_auto_20170223_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'permissions': (('can_promote', 'Can promote announcements to reach all MathSoc members (rather than members of org)'),)},
        ),
    ]
