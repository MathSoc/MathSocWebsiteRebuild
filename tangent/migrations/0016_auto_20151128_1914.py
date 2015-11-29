# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0015_auto_20151127_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='can_add_files_to_meetings',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='can_create_meetings',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='can_manage_bookings',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organization',
            name='auto_position',
            field=models.ForeignKey(related_name='+', blank=True, to='tangent.Position', null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(to='tangent.Member', null=True, blank=True),
        ),
    ]
