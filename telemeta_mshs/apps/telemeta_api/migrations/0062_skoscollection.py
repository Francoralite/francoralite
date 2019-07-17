# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0061_itemcompositor'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkosCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='nom')),
                ('uri', models.CharField(max_length=500, verbose_name='uri')),
                ('number', models.CharField(max_length=40, verbose_name='num\xe9rotation')),
                ('type', models.CharField(max_length=40, verbose_name='type')),
                ('collection', models.ForeignKey(related_name='skos_collection', default=None, blank=True, to='telemeta_api.SkosCollection', null=True, verbose_name='Collection parente')),
            ],
            options={
                'ordering': [],
                'db_table': 'skos_collection',
                'verbose_name_plural': 'skos_collections',
            },
        ),
    ]
