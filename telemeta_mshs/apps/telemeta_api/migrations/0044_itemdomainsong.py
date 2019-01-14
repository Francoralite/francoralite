# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0043_iteminformer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDomainSong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_song', models.ForeignKey(verbose_name='Genre de la chanson', to='telemeta_api.DomainSong')),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_domain_song',
                'verbose_name_plural': 'item_domain_songs',
            },
        ),
    ]