# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0068_auto_20190812_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionlanguage',
            name='collection',
            field=models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection'),
        ),
        migrations.AlterField(
            model_name='collectionlanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='language', to='telemeta_api.Language'),
        ),
        migrations.AlterModelTable(
            name='collectionlanguage',
            table='api_collection_language',
        ),
    ]
