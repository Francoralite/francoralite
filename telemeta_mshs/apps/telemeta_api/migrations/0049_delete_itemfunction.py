# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0048_usefulness'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemFunction',
        ),
    ]
