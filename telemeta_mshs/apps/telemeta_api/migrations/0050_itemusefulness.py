# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0049_delete_itemfunction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemUsefulness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
                ('usefulness', models.ForeignKey(verbose_name='Fonction', to='telemeta_api.Usefulness')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_usefulness',
                'verbose_name_plural': 'item_usefulnesses',
            },
        ),
    ]
