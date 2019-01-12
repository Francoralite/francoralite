# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0040_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCollector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('informer', models.ForeignKey(verbose_name='collector', to='telemeta_api.Authority')),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_collector',
                'verbose_name_plural': 'item_collectors',
            },
        ),
    ]
