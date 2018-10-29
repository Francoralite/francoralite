# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import telemeta.models.resource
import dirtyfields.dirtyfields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0016_auto_20181019_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcquisitionMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'acquisition',
                'verbose_name': 'acquisition mode',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Fond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.CharField(max_length=250, null=True, verbose_name='description_old', blank=True)),
                ('descriptions', models.TextField(verbose_name='description', blank=True)),
                ('code', models.CharField(unique=True, max_length=250, verbose_name='code', validators=[telemeta.models.resource.is_valid_resource_code])),
                ('public_access', models.CharField(default=b'metadata', max_length=16, verbose_name='public access', choices=[(b'none', 'none'), (b'metadata', 'metadata'), (b'mixed', 'mixed'), (b'full', 'full')])),
                ('conservation_site', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='site de conservation', blank=True)),
                ('comment', telemeta.models.fields.TextField(default=None, null=True, verbose_name='commentaires', blank=True)),
                ('acquisition_mode', models.ForeignKey(related_name='fonds', on_delete=django.db.models.deletion.SET_NULL, verbose_name="Mode d'acquisition", blank=True, to='telemeta_api.AcquisitionMode', null=True)),
            ],
            options={
                'ordering': [],
                'db_table': 'fond',
                'verbose_name_plural': 'fonds',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
