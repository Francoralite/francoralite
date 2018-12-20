# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0029_emitvox_hornbostelsachs_instrument_performancecollection_performancecollectionmusician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='typology',
            field=models.ForeignKey(verbose_name='HornbostelSachs', blank=True, to='telemeta_api.HornbostelSachs', null=True),
        ),
        migrations.AlterField(
            model_name='performancecollection',
            name='emit',
            field=models.ForeignKey(verbose_name="Nature de l'\xe9mission vocale", blank=True, to='telemeta_api.EmitVox', null=True),
        ),
        migrations.AlterField(
            model_name='performancecollection',
            name='instrument',
            field=models.ForeignKey(verbose_name='instrument', blank=True, to='telemeta_api.Instrument', null=True),
        ),
    ]
