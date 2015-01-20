# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationSeason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.ForeignKey(to='organization.Organization')),
                ('season', models.ForeignKey(to='season.Season')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organization',
            name='organizationSeasons',
            field=models.ManyToManyField(to='season.Season', through='organization.OrganizationSeason'),
            preserve_default=True,
        ),
    ]
