# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0002_auto_20161107_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(null=True, default='', blank=True)),
                ('office', models.CharField(max_length=32, default='MC 3038')),
                ('website', models.URLField(default='http://mathsoc.uwaterloo.ca')),
                ('fee', models.IntegerField(default=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='organization',
            name='members',
        ),
        migrations.RemoveField(
            model_name='organizationdocument',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='position',
            name='organization',
        ),
        migrations.AddField(
            model_name='meeting',
            name='attendance',
            field=models.ManyToManyField(to='tangent.Member', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='do_not_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='affiliate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='documents',
            field=models.ManyToManyField(to='tangent.OrganizationDocument', default=None, blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='external',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='positions',
            field=models.ManyToManyField(to='tangent.Position', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='sponsor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='primary_organization',
            field=models.ForeignKey(blank=True, default=None, to='tangent.Organization', null=True),
        ),
        migrations.RemoveField(
            model_name='position',
            name='occupied_by',
        ),
        migrations.AddField(
            model_name='position',
            name='occupied_by',
            field=models.ForeignKey(blank=True, default=None, to='tangent.Member', null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='documents',
            field=models.ManyToManyField(to='tangent.OrganizationDocument', default=None, blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(to='tangent.Member', blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='positions',
            field=models.ManyToManyField(to='tangent.Position', blank=True),
        ),
    ]
