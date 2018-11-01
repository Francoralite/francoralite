# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0020_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='code_partner',
            field=models.CharField(max_length=255, null=True, verbose_name="Cote de la mission dans l'institution partenaire", blank=True),
        ),
    ]
