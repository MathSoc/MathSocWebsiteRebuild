# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0002_auto_20150201_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_pictures', blank=True),
            preserve_default=True,
        ),
    ]
