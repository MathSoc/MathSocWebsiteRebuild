# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0012_auto_20150802_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='has_locker',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_volunteer',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='positions',
        ),
        migrations.AddField(
            model_name='organizationdocument',
            name='organization',
            field=models.ForeignKey(default=None, to='tangent.Organization'),
        ),
        migrations.AddField(
            model_name='position',
            name='organization',
            field=models.ForeignKey(default=None, to='tangent.Organization'),
        ),
    ]
