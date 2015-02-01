# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='used_resources',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='interested_in',
            field=models.ManyToManyField(to='tangent.Position', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='resume',
            field=models.FileField(null=True, upload_to=b'resumes', blank=True),
            preserve_default=True,
        ),
    ]
