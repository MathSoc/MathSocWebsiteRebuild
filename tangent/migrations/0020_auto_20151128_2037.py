# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0019_auto_20151128_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='can_join',
            new_name='want_applications',
        ),
    ]
