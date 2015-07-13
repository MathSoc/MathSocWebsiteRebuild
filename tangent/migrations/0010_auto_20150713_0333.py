# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0009_auto_20150430_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.CharField(max_length=32, choices=[(b'CLUB', b'Club'), (b'SIC', b'Special Interest Coordinator'), (b'AFFL', b'Affiliate'), (b'FACL', b'Faculty'), (b'EXTL', b'External'), (b'MATH_MISC', b'Mathematics Society'), (b'MATH_GOV', b'MathSoc Governance'), (b'COMM', b'MathSoc Committee')]),
        ),
    ]
