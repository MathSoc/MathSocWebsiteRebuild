# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0007_auto_20150201_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='documents',
            field=models.ManyToManyField(to='tangent.OrganizationDocument', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='meetings',
            field=models.ManyToManyField(to='tangent.Meeting', null=True, blank=True),
            preserve_default=True,
        ),
    ]
