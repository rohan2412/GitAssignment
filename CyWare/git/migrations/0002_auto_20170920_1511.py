# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('git', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gituser',
            name='gravatar_id',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='gituser',
            name='created_dt',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 15, 11, 9, 322043)),
        ),
        migrations.AlterField(
            model_name='gituser',
            name='updated_dt',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 15, 11, 9, 322095)),
        ),
    ]
