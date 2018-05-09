# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0002_authority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'coupe',
                'verbose_name': 'coupe',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
