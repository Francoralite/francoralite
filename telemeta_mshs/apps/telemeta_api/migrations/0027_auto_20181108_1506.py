# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0026_auto_20181108_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalRights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'api_legal_rights',
                'verbose_name': "droits d'utilisation",
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MetadataAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'metadata_author',
                'verbose_name': 'r\xe9dacteur de la fiche',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'publisher',
                'verbose_name': '\xe9diteur',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='RecordingContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'recordingcontext',
                'verbose_name': "contexte d'enregistrement",
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.RemoveField(
            model_name='collection',
            name='location',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='publisher',
        ),
        migrations.AddField(
            model_name='collection',
            name='legal_rights',
            field=models.ForeignKey(related_name='collection', on_delete=django.db.models.deletion.SET_NULL, verbose_name="Droits d'utilisation", blank=True, to='telemeta_api.LegalRights', null=True),
        ),
    ]
