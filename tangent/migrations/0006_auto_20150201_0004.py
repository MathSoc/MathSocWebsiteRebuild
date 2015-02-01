# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tangent.models


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0005_auto_20150131_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='number',
        ),
        migrations.AddField(
            model_name='meeting',
            name='budget',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='agenda',
            field=models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='minutes',
            field=models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.CharField(max_length=8, choices=[(b'CLUB', b'Club'), (b'SIC', b'Special Interest Coordinator'), (b'AFF', b'Affiliate'), (b'FAC', b'Faculty'), (b'ECOM', b'External'), (b'MATHSOC', b'Mathematics Society'), (b'COUNCIL', b'MathSoc Council'), (b'OFFICE', b'MathSoc Office')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='fee',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='member_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='office',
            field=models.CharField(default=b'MC 3038', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(default=b'http://mathsoc.uwaterloo.ca'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationdocument',
            name='description',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='description',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='website',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
    ]
