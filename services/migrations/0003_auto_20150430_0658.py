# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20150201_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevaluation',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='course_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='semester',
            field=models.IntegerField(),
        ),
    ]
