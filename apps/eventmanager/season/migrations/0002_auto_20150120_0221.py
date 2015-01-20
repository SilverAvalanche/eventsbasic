# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='season',
            old_name='seasonDescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='seasonEnd',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='seasonName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='seasonStart',
            new_name='start',
        ),
        migrations.AddField(
            model_name='season',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
