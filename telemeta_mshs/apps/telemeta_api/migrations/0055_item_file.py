# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0054_itemmusicalgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='file',
            field=models.FileField(default='test.mp3', upload_to=b'items/%Y/%m/%d', max_length=1024, verbose_name='fichier son', db_column=b'filename'),
            preserve_default=False,
        ),
    ]
