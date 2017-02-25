# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0004_position_is_superuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'permissions': ('can_promote', 'Can promote announcements to reach all MathSoc members (rather than members of org)')},
        ),
        migrations.AlterModelOptions(
            name='baseorg',
            options={'permissions': (('add_announcements', 'Can post announcements belonging to org'), ('manage_announcement', 'Can edit announcements belonging to org'), ('attach_positions', 'Can attach members to positions/add members in the org'), ('add_meetings', 'Can add meetings to the org'), ('manage_meetings', 'Can manage meetings (not created by themselves) within the org'), ('add_documents', 'Can add documents beloging to the org'), ('manage_documents', 'Can manage documents belonging to the org'))},
        ),
    ]
