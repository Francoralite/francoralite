# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0057_auto_20190301_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTranscodingFlag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mime_type', models.CharField(default=b'', max_length=255, verbose_name='type MIME')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('value', models.BooleanField(verbose_name='Transcod\xe9')),
                ('item', models.ForeignKey(related_name='trancoded', verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_transcoding_flag',
                'verbose_name_plural': 'item_transcoding_flags',
            },
        ),
    ]
