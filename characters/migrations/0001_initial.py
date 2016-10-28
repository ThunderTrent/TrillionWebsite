# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('characterName', models.CharField(max_length=255, null=True, verbose_name=b'Church Name:', db_column=b'churchName', blank=True)),
                ('server', models.CharField(max_length=255, null=True, db_column=b'serverName', blank=True)),
                ('level', models.IntegerField(max_length=255, null=True, db_column=b'characterLevel', blank=True)),
                ('itemLevel', models.IntegerField(max_length=255, null=True, db_column=b'itemLevel', blank=True)),
                ('lastArmoryUpdate', models.DateTimeField(max_length=255, null=True, db_column=b'lastArmoryUpdate', blank=True)),
                ('lastWLUpdate', models.DateTimeField(max_length=255, null=True, verbose_name=b'Last Warcraft Logs Update', db_column=b'lastWLUpdate', blank=True)),
                ('description', models.CharField(max_length=255, null=True, verbose_name=b'Character Description', db_column=b'description', blank=True)),
            ],
        ),
    ]
