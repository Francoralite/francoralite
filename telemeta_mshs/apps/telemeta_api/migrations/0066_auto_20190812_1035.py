# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0065_auto_20190806_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionlocation',
            name='location',
            field=telemeta.models.fields.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='location', to='telemeta_api.Location'),
        ),
    ]
