# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=200)),
                ('git_id', models.IntegerField(unique=True)),
                ('avatar_url', models.URLField()),
                ('url', models.URLField()),
                ('html_url', models.URLField()),
                ('followers_url', models.URLField()),
                ('following_url', models.URLField()),
                ('site_admin', models.BooleanField(default=False)),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
