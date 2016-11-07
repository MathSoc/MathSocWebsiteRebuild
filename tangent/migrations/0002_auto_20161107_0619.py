# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='affiliations',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='classification',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='fee',
        ),
    ]
