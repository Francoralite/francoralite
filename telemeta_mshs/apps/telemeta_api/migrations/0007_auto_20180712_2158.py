# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0006_auto_20180712_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioncollectors',
            name='collection',
            field=telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta.MediaCollection'),
        ),
    ]
