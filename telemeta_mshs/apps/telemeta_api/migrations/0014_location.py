# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0013_auto_20181017_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='code', blank=True)),
                ('name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='name', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=None, null=True, verbose_name='notes', blank=True)),
                ('latitude', telemeta.models.fields.FloatField(default=None, null=True, blank=True)),
                ('longitude', telemeta.models.fields.FloatField(default=None, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
