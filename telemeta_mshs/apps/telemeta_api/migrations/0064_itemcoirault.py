# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0063_skosconcept'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCoirault',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coirault', models.ForeignKey(verbose_name='Coirault', to='telemeta_api.SkosConcept')),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_coirault',
                'verbose_name_plural': 'item_coiraults',
            },
        ),
    ]
