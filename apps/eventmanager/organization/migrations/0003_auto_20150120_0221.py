# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20150120_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 2, 21, 9, 204057, tzinfo=utc), auto_now=True, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
