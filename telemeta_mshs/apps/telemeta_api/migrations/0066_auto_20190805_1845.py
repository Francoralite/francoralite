# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0065_auto_20190802_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='public_access',
        ),
        migrations.AlterField(
            model_name='collection',
            name='code',
            field=models.CharField(max_length=255, verbose_name='cote', validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}$', message=b'Code must conform to XXXX_XXX_000X_0000', code=b'invalid_code')]),
        ),
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(max_length=255, verbose_name='titre'),
        ),
    ]
