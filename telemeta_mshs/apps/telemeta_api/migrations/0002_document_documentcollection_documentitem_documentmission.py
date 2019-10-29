# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_nakala', models.CharField(max_length=25, verbose_name='ID Nakala')),
                ('title', models.CharField(max_length=255, verbose_name='titre')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('credits', models.TextField(null=True, verbose_name='cr\xe9dits', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'api_document',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentCollection',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='telemeta_api.Document')),
                ('collection', models.ForeignKey(related_name='related_document', verbose_name='collection', to='telemeta_api.Collection')),
            ],
            options={
                'ordering': ['collection', 'title'],
                'db_table': 'api_document_collection',
                'verbose_name_plural': 'document',
            },
            bases=('telemeta_api.document',),
        ),
        migrations.CreateModel(
            name='DocumentItem',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='telemeta_api.Document')),
                ('item', models.ForeignKey(related_name='related_document', verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': ['item', 'title'],
                'db_table': 'api_document_item',
                'verbose_name_plural': 'document',
            },
            bases=('telemeta_api.document',),
        ),
        migrations.CreateModel(
            name='DocumentMission',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='telemeta_api.Document')),
                ('mission', models.ForeignKey(related_name='related_document', verbose_name='mission', to='telemeta_api.Mission')),
            ],
            options={
                'ordering': ['mission', 'title'],
                'db_table': 'api_document_mission',
                'verbose_name_plural': 'document',
            },
            bases=('telemeta_api.document',),
        ),
    ]
