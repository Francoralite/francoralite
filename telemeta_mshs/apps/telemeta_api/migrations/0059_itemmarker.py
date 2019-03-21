# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('telemeta_api', '0058_itemtranscodingflag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.FloatField()),
                ('title', models.CharField(default=b'', max_length=255, verbose_name='nom', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('author', models.ForeignKey(related_name='api_markers', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('item', models.ForeignKey(related_name='marker', verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_marker',
                'verbose_name_plural': 'item_markers',
            },
        ),
    ]
