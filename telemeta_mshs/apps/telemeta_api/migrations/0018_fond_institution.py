# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0017_acquisitionmode_fond'),
    ]

    operations = [
        migrations.AddField(
            model_name='fond',
            name='institution',
            field=models.ForeignKey(related_name='fonds', default=1, verbose_name='Institution', to='telemeta_api.Institution'),
            preserve_default=False,
        ),
    ]
