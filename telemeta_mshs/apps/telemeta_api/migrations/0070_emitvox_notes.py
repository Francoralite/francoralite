# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0069_auto_20190812_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='emitvox',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
    ]
