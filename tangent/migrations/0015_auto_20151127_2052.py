# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0014_organization_auto_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='member_count',
        ),
        migrations.AddField(
            model_name='organization',
            name='can_join',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(default=None, to='tangent.Member'),
        ),
        migrations.AddField(
            model_name='position',
            name='can_edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='can_post',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='position',
            name='occupied_by',
        ),
        migrations.AddField(
            model_name='position',
            name='occupied_by',
            field=models.ManyToManyField(default=None, to='tangent.Member'),
        ),
    ]
