# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20150430_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calendar_id', models.CharField(max_length=256)),
                ('requesting_id', models.CharField(max_length=16)),
                ('contact_name', models.CharField(max_length=256)),
                ('contact_email', models.CharField(max_length=256)),
                ('contact_phone', models.CharField(max_length=256)),
                ('organisation', models.CharField(max_length=256)),
                ('event_name', models.CharField(max_length=256)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
    ]
