# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0018_fond_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='fond',
            name='code_partner',
            field=telemeta.models.fields.CharField(default=None, max_length=250, null=True, verbose_name="Cote dans l'institution partenaire", blank=True),
        ),
        migrations.AlterField(
            model_name='fond',
            name='conservation_site',
            field=telemeta.models.fields.CharField(default=None, max_length=250, null=True, verbose_name='lieu de conservation original', blank=True),
        ),
    ]
