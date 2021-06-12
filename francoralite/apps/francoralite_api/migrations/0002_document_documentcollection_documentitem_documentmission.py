# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('francoralite_api', '0001_initial'),
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
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='francoralite_api.Document', on_delete=models.CASCADE)),
                ('collection', models.ForeignKey(related_name='related_document', verbose_name='collection', to='francoralite_api.Collection', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['collection', 'title'],
                'db_table': 'api_document_collection',
                'verbose_name_plural': 'document',
            },
            bases=('francoralite_api.document',),
        ),
        migrations.CreateModel(
            name='DocumentItem',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='francoralite_api.Document', on_delete=models.CASCADE)),
                ('item', models.ForeignKey(related_name='related_document', verbose_name='item', to='francoralite_api.Item', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['item', 'title'],
                'db_table': 'api_document_item',
                'verbose_name_plural': 'document',
            },
            bases=('francoralite_api.document',),
        ),
        migrations.CreateModel(
            name='DocumentMission',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='francoralite_api.Document', on_delete=models.CASCADE)),
                ('mission', models.ForeignKey(related_name='related_document', verbose_name='mission', to='francoralite_api.Mission', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['mission', 'title'],
                'db_table': 'api_document_mission',
                'verbose_name_plural': 'document',
            },
            bases=('francoralite_api.document',),
        ),
    ]
