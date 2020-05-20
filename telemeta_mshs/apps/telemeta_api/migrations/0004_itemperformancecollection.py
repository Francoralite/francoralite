# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0003_documentfond'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPerformanceCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
                ('performance_collection', models.ForeignKey(verbose_name='performance', to='telemeta_api.PerformanceCollection')),
            ],
            options={
                'ordering': [],
                'db_table': 'item_performance_collection',
                'verbose_name_plural': 'interpretes',
            },
        ),
    ]
