# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0004_itemperformance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemanalysis',
            name='item',
        ),
        migrations.RemoveField(
            model_name='itemmarker',
            name='author',
        ),
        migrations.RemoveField(
            model_name='itemmarker',
            name='item',
        ),
        migrations.RemoveField(
            model_name='itemtranscodingflag',
            name='item',
        ),
        migrations.DeleteModel(
            name='ItemAnalysis',
        ),
        migrations.DeleteModel(
            name='ItemMarker',
        ),
        migrations.DeleteModel(
            name='ItemTranscodingFlag',
        ),
    ]
