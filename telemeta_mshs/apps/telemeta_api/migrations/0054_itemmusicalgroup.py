# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0053_itemmusicalorganization'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMusicalGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
                ('musical_group', models.ForeignKey(verbose_name='Fonction', to='telemeta_api.MusicalGroup')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_musical_group',
                'verbose_name_plural': 'item_musical_groups',
            },
        ),
    ]
