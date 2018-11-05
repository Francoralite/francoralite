# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import telemeta.models.resource
import dirtyfields.dirtyfields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0022_extmediacollection_mission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.CharField(max_length=250, null=True, verbose_name='description_old', blank=True)),
                ('descriptions', models.TextField(verbose_name='description', blank=True)),
                ('code', models.CharField(unique=True, max_length=250, verbose_name='code', validators=[telemeta.models.resource.is_valid_resource_code])),
                ('public_access', models.CharField(default=b'metadata', max_length=16, verbose_name='public access', choices=[(b'none', 'none'), (b'metadata', 'metadata'), (b'mixed', 'mixed'), (b'full', 'full')])),
                ('alt_title', models.CharField(max_length=255, verbose_name='Titre original')),
                ('recording_context', models.CharField(max_length=255, verbose_name="Contexte d'enregistrement")),
                ('recorded_from_year', models.DateField(null=True)),
                ('recorded_to_year', models.DateField(null=True)),
                ('year_published', models.IntegerField(null=True)),
                ('location_details', models.TextField(default=b'', verbose_name='Pr\xe9cisions sur le lieu', blank=True)),
                ('cultural_area', models.CharField(default=b'', help_text='Aire culturelle ; Aire culturelle', max_length=255, verbose_name='Aire culturelle', blank=True)),
                ('language', models.CharField(default=b'', help_text='Langage ; langage', max_length=255, verbose_name=b'langage', blank=True)),
                ('editor', models.CharField(default=b'', help_text='\xe9diteur ; \xe9diteur', max_length=255, verbose_name='Editeur', blank=True)),
                ('editor_collection', models.CharField(default=b'', help_text=b'collection ; collection', max_length=255, verbose_name='Collection \xe9diteur', blank=True)),
                ('metadata_writer', models.CharField(default=b'', help_text='R\xe9dacteur ; r\xe9dacteur', max_length=255, verbose_name='R\xe9dacteur(s) fiches ou registre', blank=True)),
                ('code_partner', models.CharField(max_length=255, null=True, verbose_name="Cote dans l'institution partenaire", blank=True)),
                ('comment', models.TextField(null=True, verbose_name='commentaires', blank=True)),
                ('location', models.ForeignKey(related_name='location', on_delete=django.db.models.deletion.SET_NULL, verbose_name='lieu', blank=True, to='telemeta_api.Location', null=True)),
                ('mission', models.ForeignKey(related_name='collection', default=b'', verbose_name='Mission', blank=True, to='telemeta_api.Mission')),
            ],
            options={
                'db_table': 'int_collection',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.RemoveField(
            model_name='extmediacollection',
            name='media_collection',
        ),
        migrations.RemoveField(
            model_name='extmediacollection',
            name='mission',
        ),
        migrations.AlterModelOptions(
            name='collectioncollectors',
            options={'ordering': [], 'verbose_name_plural': 'collection_collectors'},
        ),
        migrations.AlterField(
            model_name='collectioncollectors',
            name='collection',
            field=telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta_api.Collection'),
        ),
        migrations.AlterField(
            model_name='collectioninformer',
            name='collection',
            field=telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta_api.Collection'),
        ),
        migrations.AlterField(
            model_name='collectionlanguage',
            name='collection',
            field=telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta_api.Collection'),
        ),
        migrations.AlterField(
            model_name='collectionlocation',
            name='collection',
            field=telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta_api.Collection'),
        ),
        migrations.AlterField(
            model_name='collectionlocation',
            name='location',
            field=telemeta.models.fields.ForeignKey(verbose_name='location', to='telemeta_api.Location'),
        ),
        migrations.AlterField(
            model_name='collectionpublisher',
            name='collection',
            field=telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta_api.Collection'),
        ),
        migrations.AlterModelTable(
            name='collectioncollectors',
            table='collection_collector',
        ),
        migrations.DeleteModel(
            name='ExtMediaCollection',
        ),
    ]
