# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('git', '0003_auto_20170920_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gituser',
            name='created_dt',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 11, 29, 34, 54463)),
        ),
        migrations.AlterField(
            model_name='gituser',
            name='score',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gituser',
            name='updated_dt',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 11, 29, 34, 54500)),
        ),
    ]
