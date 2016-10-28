# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, db_column=b'id'),
        ),
        migrations.AlterField(
            model_name='character',
            name='itemLevel',
            field=models.IntegerField(null=True, db_column=b'itemLevel', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(null=True, db_column=b'characterLevel', blank=True),
        ),
    ]
