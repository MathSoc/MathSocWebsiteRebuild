# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tangent.models


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0009_auto_20150201_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='meeting',
            name='budget_file',
            field=models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True),
            preserve_default=True,
        ),
    ]
