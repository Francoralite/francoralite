# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0071_auto_20190925_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='notes',
            field=models.TextField(null=True, verbose_name='notes', blank=True),
        ),
    ]
