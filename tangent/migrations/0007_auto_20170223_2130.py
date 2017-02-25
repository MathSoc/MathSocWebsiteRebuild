# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0006_auto_20170223_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseorg',
            options={},
        ),
        migrations.AlterModelOptions(
            name='club',
            options={'permissions': (('add_announcements', 'Can post announcements belonging to org'), ('manage_announcement', 'Can edit announcements belonging to org'), ('attach_positions', 'Can attach members to positions/add members in the org'), ('add_meetings', 'Can add meetings to the org'), ('manage_meetings', 'Can manage meetings (not created by themselves) within the org'), ('add_documents', 'Can add documents beloging to the org'), ('manage_documents', 'Can manage documents belonging to the org'))},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'permissions': (('add_announcements', 'Can post announcements belonging to org'), ('manage_announcement', 'Can edit announcements belonging to org'), ('attach_positions', 'Can attach members to positions/add members in the org'), ('add_meetings', 'Can add meetings to the org'), ('manage_meetings', 'Can manage meetings (not created by themselves) within the org'), ('add_documents', 'Can add documents beloging to the org'), ('manage_documents', 'Can manage documents belonging to the org'))},
        ),
    ]
