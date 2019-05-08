# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0060_itemauthor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCompositor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compositor', models.ForeignKey(verbose_name='XXXXXX', to='telemeta_api.Authority')),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_compositor',
                'verbose_name_plural': 'item_compositors',
            },
        ),
    ]
