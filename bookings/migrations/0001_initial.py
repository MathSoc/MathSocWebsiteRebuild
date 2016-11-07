# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('calendar_id', models.CharField(max_length=256)),
                ('calendar', models.CharField(max_length=256)),
                ('requesting_id', models.CharField(max_length=16)),
                ('contact_name', models.CharField(max_length=256)),
                ('contact_email', models.CharField(max_length=256)),
                ('contact_phone', models.CharField(max_length=256)),
                ('organisation', models.CharField(max_length=256)),
                ('event_name', models.CharField(max_length=256)),
                ('status', models.IntegerField(choices=[(1, 'Requested'), (2, 'Accepted'), (3, 'Rejected')], default=1)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
    ]
