# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0003_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='organization',
        ),
        migrations.AddField(
            model_name='organization',
            name='admin',
            field=models.ManyToManyField(related_name='admin', to='tangent.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='description',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='meetings',
            field=models.ManyToManyField(to='tangent.Meeting'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='positions',
            field=models.ManyToManyField(related_name='position', to='tangent.Position'),
            preserve_default=True,
        ),
    ]
