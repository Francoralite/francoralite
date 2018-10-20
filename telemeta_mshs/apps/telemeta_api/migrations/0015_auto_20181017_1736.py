# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0014_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='birth_location',
            field=telemeta.models.fields.ForeignKey(related_name='birth_location', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='telemeta_api.Location', null=True, verbose_name='birth location'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='death_location',
            field=telemeta.models.fields.ForeignKey(related_name='death_location', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='telemeta_api.Location', null=True, verbose_name='death location'),
        ),
    ]
