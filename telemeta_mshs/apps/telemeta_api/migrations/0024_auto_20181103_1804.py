# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0023_auto_20181102_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'mediatype',
                'verbose_name': 'mediatype',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='metadata_writer',
            new_name='metadata_author',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='editor',
            new_name='publisher',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='editor_collection',
            new_name='publisher_collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='auto_period_access',
            field=models.BooleanField(default=True, verbose_name='Acc\xe8s automatique apr\xe8s la date glissante'),
        ),
        migrations.AddField(
            model_name='collection',
            name='booklet_author',
            field=models.CharField(default=b'', help_text="Nom de l'auteur", max_length=255, verbose_name='Auteur de la note \xe9dit\xe9e', blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='physical_items_num',
            field=models.IntegerField(null=True, verbose_name='Nombre de composants (support / pi\xe8ce)'),
        ),
        migrations.AddField(
            model_name='collection',
            name='media_type',
            field=models.ForeignKey(related_name='collection', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Type de m\xe9dia', blank=True, to='telemeta_api.MediaType', null=True),
        ),
    ]
