# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0056_item_analysis'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item_analysis',
            ),
        migrations.CreateModel(
            name='ItemAnalysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element_type', models.CharField(default=b'analysis', max_length=255, verbose_name='type element')),
                ('analyzer_id', models.CharField(default=b'', max_length=255, verbose_name='id', blank=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='nom', blank=True)),
                ('value', models.CharField(default=b'', max_length=255, verbose_name='valeur', blank=True)),
                ('unit', models.CharField(default=b'', max_length=255, verbose_name='unit\xe9', blank=True)),
                ('item', models.ForeignKey(related_name='analysis', verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_analysis',
                'verbose_name_plural': 'item_analysises',
            },
        ),
    ]
