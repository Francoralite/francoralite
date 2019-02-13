# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0045_itemdomainmusic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDomainVocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_vocal', models.ForeignKey(verbose_name="Genre de l'autre expression vocale", to='telemeta_api.DomainVocal')),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_domain_vocal',
                'verbose_name_plural': 'item_domain_vocals',
            },
        ),
    ]
