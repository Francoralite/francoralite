# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0021_auto_20181031_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='extmediacollection',
            name='mission',
            field=models.ForeignKey(related_name='collection', default=b'', verbose_name='Mission', blank=True, to='telemeta_api.Mission'),
        ),
    ]
