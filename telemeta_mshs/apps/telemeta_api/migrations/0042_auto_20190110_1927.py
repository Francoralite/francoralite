# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0041_itemcollector'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcollector',
            old_name='informer',
            new_name='collector',
        ),
    ]
