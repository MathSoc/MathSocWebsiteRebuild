# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('tangent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='can_add_files_to_meetings',
        ),
        migrations.RemoveField(
            model_name='position',
            name='can_create_meetings',
        ),
        migrations.RemoveField(
            model_name='position',
            name='can_edit',
        ),
        migrations.RemoveField(
            model_name='position',
            name='can_manage_bookings',
        ),
        migrations.RemoveField(
            model_name='position',
            name='can_post',
        ),
        migrations.RemoveField(
            model_name='position',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='position',
            name='permissions_group',
            field=models.ForeignKey(default=None, blank=True, null=True, to='auth.Group'),
        ),
    ]
