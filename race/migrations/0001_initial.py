# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('race_id', models.AutoField(serialize=False, primary_key=True)),
                ('race_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('race_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
