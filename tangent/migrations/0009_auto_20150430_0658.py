# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0008_member_cover_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='interested_in',
            field=models.ManyToManyField(to='tangent.Position', blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='documents',
            field=models.ManyToManyField(to='tangent.OrganizationDocument', blank=True),
        ),
    ]
