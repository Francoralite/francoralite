# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0070_emitvox_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='notes',
            field=telemeta.models.fields.TextField(default=None, null=True, verbose_name='notes', blank=True),
        ),
    ]
