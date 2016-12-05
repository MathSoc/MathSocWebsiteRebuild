# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('locker_number', models.IntegerField(primary_key=True, unique=True, serialize=False)),
                ('current_combo', models.CharField(max_length=6)),
                ('combo_number', models.IntegerField()),
                ('combo0', models.CharField(max_length=6)),
                ('combo1', models.CharField(max_length=6)),
                ('combo2', models.CharField(max_length=6)),
                ('combo3', models.CharField(max_length=6)),
                ('combo4', models.CharField(max_length=6)),
                ('owner', models.ForeignKey(to='tangent.Member', null=True, blank=True)),
            ],
        ),
    ]
