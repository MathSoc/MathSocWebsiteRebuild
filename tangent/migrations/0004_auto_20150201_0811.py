# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0003_member_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='end_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='occupied_by',
            field=models.ForeignKey(blank=True, to='tangent.Member', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='start_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
