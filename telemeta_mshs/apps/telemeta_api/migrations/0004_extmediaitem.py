# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0006_enumerationproperty'),
        ('telemeta_api', '0003_coupe'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtMediaItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_item', models.OneToOneField(to='telemeta.MediaItem')),
                ('mshs_ch_coupe', models.ForeignKey(verbose_name='coupe', blank=True, to='telemeta_api.Coupe', null=True)),
            ],
            options={
                'db_table': 'ext_media_item',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
