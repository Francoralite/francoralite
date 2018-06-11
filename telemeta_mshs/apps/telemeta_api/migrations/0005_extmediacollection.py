# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0006_enumerationproperty'),
        ('telemeta_api', '0004_extmediaitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtMediaCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_details', markdownx.models.MarkdownxField(blank=True)),
                ('cultural_area', models.TextField(help_text='Aire culturelle ; Aire culturelle', verbose_name='cultural area')),
                ('language', models.TextField(help_text='Langage ; langage', verbose_name=b'langage')),
                ('collectors', models.ManyToManyField(related_name='collectors', null=True, verbose_name='collectors', to='telemeta_api.Authority', blank=True)),
                ('informers', models.ManyToManyField(related_name='informers', null=True, verbose_name='informers', to='telemeta_api.Authority', blank=True)),
                ('language_iso', models.ManyToManyField(related_name='collections', null=True, verbose_name='Language (ISO norm)', to='telemeta.Language', blank=True)),
                ('location', models.ManyToManyField(related_name='locations', null=True, verbose_name='location', to='telemeta.Location', blank=True)),
                ('media_collection', models.OneToOneField(to='telemeta.MediaCollection')),
                ('publishers', models.ManyToManyField(related_name='publishers', null=True, verbose_name='publishers', to='telemeta.Publisher', blank=True)),
            ],
            options={
                'db_table': 'ext_media_collection',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
