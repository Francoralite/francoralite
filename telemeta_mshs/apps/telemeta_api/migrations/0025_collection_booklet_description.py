# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0024_auto_20181103_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='booklet_description',
            field=models.TextField(null=True, verbose_name='Documentation associ\xe9e', blank=True),
        ),
    ]
