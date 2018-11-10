# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0025_collection_booklet_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='alt_title',
            field=models.CharField(max_length=255, verbose_name='Titre original', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='physical_items_num',
            field=models.IntegerField(null=True, verbose_name='Nombre de composants (support / pi\xe8ce)', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='recorded_from_year',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='recorded_to_year',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='recording_context',
            field=models.CharField(max_length=255, verbose_name="Contexte d'enregistrement", blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='year_published',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
