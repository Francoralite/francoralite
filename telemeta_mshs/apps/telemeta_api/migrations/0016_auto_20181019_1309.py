# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0015_auto_20181017_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='birth_location',
            field=models.ForeignKey(related_name='birth_location', on_delete=django.db.models.deletion.SET_NULL, verbose_name='birth location', blank=True, to='telemeta_api.Location', null=True),
        ),
        migrations.AlterField(
            model_name='authority',
            name='death_location',
            field=models.ForeignKey(related_name='death_location', on_delete=django.db.models.deletion.SET_NULL, verbose_name='death location', blank=True, to='telemeta_api.Location', null=True),
        ),
    ]
