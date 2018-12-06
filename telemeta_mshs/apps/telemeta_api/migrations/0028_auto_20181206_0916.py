# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0027_auto_20181108_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpublisher',
            name='publisher',
            field=telemeta.models.fields.ForeignKey(verbose_name='publisher', to='telemeta_api.Publisher'),
        ),
    ]
