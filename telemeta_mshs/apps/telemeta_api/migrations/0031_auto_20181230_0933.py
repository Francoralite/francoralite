# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0030_auto_20181207_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_musical_organization',
                'verbose_name_plural': 'musical_organizations',
            },
        ),
        migrations.AlterModelOptions(
            name='emitvox',
            options={'ordering': [], 'verbose_name_plural': 'nature des emissions vocales'},
        ),
        migrations.AlterModelOptions(
            name='metadataauthor',
            options={'ordering': ['value'], 'verbose_name': 'redacteur de la fiche'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['value'], 'verbose_name': 'editeur'},
        ),
    ]
