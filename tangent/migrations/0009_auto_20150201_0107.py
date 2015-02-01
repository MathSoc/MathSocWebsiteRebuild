# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0008_auto_20150201_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.CharField(max_length=32, choices=[(b'Club', b'Club'), (b'Special Interest Coordinator', b'Special Interest Coordinator'), (b'Affiliate', b'Affiliate'), (b'Faculty', b'Faculty'), (b'External', b'External'), (b'Mathematics Society', b'Mathematics Society'), (b'MathSoc Council', b'MathSoc Council'), (b'MathSoc Office', b'MathSoc Office')]),
            preserve_default=True,
        ),
    ]
