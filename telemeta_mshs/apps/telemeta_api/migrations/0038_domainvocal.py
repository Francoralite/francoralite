# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0037_domainmusic'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainVocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_domain_vocal',
                'verbose_name_plural': 'domain_vocals',
            },
        ),
    ]
