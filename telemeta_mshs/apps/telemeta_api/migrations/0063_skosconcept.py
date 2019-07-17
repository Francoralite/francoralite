# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0062_skoscollection'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkosConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='nom')),
                ('uri', models.CharField(max_length=500, verbose_name='uri')),
                ('number', models.CharField(max_length=40, verbose_name='num\xe9rotation')),
                ('abstract', models.TextField(null=True, blank=True)),
                ('collection', models.ForeignKey(related_name='skos_concept', default=None, verbose_name='Collection parente', to='telemeta_api.SkosCollection')),
            ],
            options={
                'ordering': ['number'],
                'db_table': 'skos_concept',
                'verbose_name_plural': 'skos_concepts',
            },
        ),
    ]
