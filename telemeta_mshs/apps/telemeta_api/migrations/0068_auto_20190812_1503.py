# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0067_auto_20190812_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='comment',
            field=models.TextField(null=True, verbose_name='comment', blank=True),
        ),
    ]
