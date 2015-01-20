# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrant',
            old_name='registrantEmail',
            new_name='email',
        ),
        migrations.AddField(
            model_name='registrant',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
