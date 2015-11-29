# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0013_auto_20151126_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='auto_position',
            field=models.ForeignKey(related_name='+', default=None, to='tangent.Position'),
        ),
    ]
