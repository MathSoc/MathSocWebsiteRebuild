# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0021_auto_20151128_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='auto_position',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.CharField(default='Comfy Lounge', max_length=256),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='term',
            field=models.CharField(choices=[('W', 'Winter'), ('S', 'Spring'), ('F', 'Fall')], max_length=2),
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='cover_letter',
            field=models.TextField(blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='member',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.CharField(choices=[('CLUB', 'Club'), ('SIC', 'Special Interest Coordinator'), ('AFFL', 'Affiliate'), ('FACL', 'Faculty'), ('EXTL', 'External'), ('MATH_MISC', 'Mathematics Society'), ('MATH_GOV', 'MathSoc Governance'), ('COMM', 'MathSoc Committee')], max_length=32),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='organization',
            name='office',
            field=models.CharField(default='MC 3038', max_length=32),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(default='http://mathsoc.uwaterloo.ca'),
        ),
        migrations.AlterField(
            model_name='organizationdocument',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='website',
            field=models.URLField(default=''),
        ),
    ]
