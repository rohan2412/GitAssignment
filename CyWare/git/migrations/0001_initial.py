# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2017, 9, 20, 15, 8, 40, 370685))),
                ('updated_dt', models.DateTimeField(default=datetime.datetime(2017, 9, 20, 15, 8, 40, 370727))),
                ('login', models.CharField(max_length=200)),
                ('git_id', models.IntegerField(unique=True)),
                ('avatar_url', models.URLField()),
                ('url', models.URLField()),
                ('html_url', models.URLField()),
                ('followers_url', models.URLField()),
                ('following_url', models.URLField()),
                ('gists_url', models.URLField()),
                ('starred_url', models.URLField()),
                ('subscriptions_url', models.URLField()),
                ('organizations_url', models.URLField()),
                ('repos_url', models.URLField()),
                ('events_url', models.URLField()),
                ('received_events_url', models.URLField()),
                ('type', models.CharField(default=b'User', max_length=50)),
                ('site_admin', models.BooleanField(default=False)),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
