# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0028_auto_20181206_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmitVox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name="Nature de l'\xe9mission vocale")),
            ],
            options={
                'ordering': [],
                'db_table': 'emit_vox',
                'verbose_name_plural': 'nature des \xe9missions vocales',
            },
        ),
        migrations.CreateModel(
            name='HornbostelSachs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(unique=True, max_length=30, verbose_name='Num\xe9rotation')),
                ('name', models.TextField(null=True, verbose_name='Nom', blank=True)),
            ],
            options={
                'ordering': [],
                'db_table': 'hornbostelsachs',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
                ('typology', models.ForeignKey(verbose_name='HornbostelSachs', to='telemeta_api.HornbostelSachs')),
            ],
            options={
                'ordering': [],
                'db_table': 'instrument',
                'verbose_name_plural': 'instruments',
            },
        ),
        migrations.CreateModel(
            name='PerformanceCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name='Nombre')),
                ('collection', models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection')),
                ('emit', models.ForeignKey(verbose_name="Nature de l'\xe9mission vocale", to='telemeta_api.EmitVox')),
                ('instrument', models.ForeignKey(verbose_name='instrument', to='telemeta_api.Instrument')),
            ],
            options={
                'ordering': [],
                'db_table': 'performance_collection',
                'verbose_name_plural': 'interpretes',
            },
        ),
        migrations.CreateModel(
            name='PerformanceCollectionMusician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('musician', models.ForeignKey(verbose_name='musician', to='telemeta_api.Authority')),
                ('performance_collection', models.ForeignKey(verbose_name='performance', to='telemeta_api.PerformanceCollection')),
            ],
            options={
                'ordering': [],
                'db_table': 'performance_collection_musician',
                'verbose_name_plural': 'musicians',
            },
        ),
    ]
