# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0046_itemdomainvocal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDomainTale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_tale', models.ForeignKey(verbose_name='Genre du conte', to='telemeta_api.DomainTale')),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_domain_tale',
                'verbose_name_plural': 'item_domain_tales',
            },
        ),
    ]
