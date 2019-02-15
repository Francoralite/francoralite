# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0051_itemdance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemThematic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
                ('thematic', models.ForeignKey(verbose_name='Fonction', to='telemeta_api.Thematic')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_thematic',
                'verbose_name_plural': 'item_thematics',
            },
        ),
    ]
