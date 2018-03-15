# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
#        ('telemeta', '0006_enumerationproperty')
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='name', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'institutions',
                'verbose_name_plural': 'institutions',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
