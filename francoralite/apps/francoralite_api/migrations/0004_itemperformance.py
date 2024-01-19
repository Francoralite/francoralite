# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('francoralite_api', '0003_documentfond'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPerformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='item', to='francoralite_api.Item', on_delete=models.CASCADE)),
                ('performance', models.ForeignKey(verbose_name='performance', to='francoralite_api.PerformanceCollection', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': [],
                'db_table': 'item_performance',
                'verbose_name_plural': 'item_performance',
            },
        ),
    ]
