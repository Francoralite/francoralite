# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta_mshs.apps.telemeta_api.models.ext_media_item
import dirtyfields.dirtyfields
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('telemeta', '0006_enumerationproperty'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcquisitionMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_acquisition',
                'verbose_name_plural': 'acquisitions',
            },
        ),
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('civility', models.CharField(max_length=255, verbose_name='civility', blank=True)),
                ('alias', models.CharField(max_length=255, verbose_name='alias', blank=True)),
                ('is_collector', models.BooleanField(default=False, verbose_name='collector')),
                ('is_informer', models.BooleanField(default=False, verbose_name='informer')),
                ('is_author', models.BooleanField(default=False, verbose_name='author')),
                ('is_composer', models.BooleanField(default=False, verbose_name='composer')),
                ('is_editor', models.BooleanField(default=False, verbose_name='editor')),
                ('birth_date', models.DateField(null=True)),
                ('death_date', models.DateField(null=True)),
                ('biography', models.TextField(null=True, verbose_name='biography', blank=True)),
                ('uri', models.URLField(null=True, verbose_name='URI', blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'db_table': 'authority',
                'verbose_name_plural': 'authorities',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='titre')),
                ('alt_title', models.CharField(max_length=255, verbose_name='Titre original', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('recording_context', models.CharField(max_length=255, verbose_name="Contexte d'enregistrement", blank=True)),
                ('recorded_from_year', models.DateField(null=True, blank=True)),
                ('recorded_to_year', models.DateField(null=True, blank=True)),
                ('year_published', models.IntegerField(null=True, blank=True)),
                ('location_details', models.TextField(default=b'', verbose_name='Pr\xe9cisions sur le lieu', blank=True)),
                ('cultural_area', models.CharField(default=b'', help_text='Aire culturelle ; Aire culturelle', max_length=255, verbose_name='Aire culturelle', blank=True)),
                ('language', models.CharField(default=b'', help_text='Langage ; langage', max_length=255, verbose_name=b'langage', blank=True)),
                ('publisher_collection', models.CharField(default=b'', help_text=b'collection ; collection', max_length=255, verbose_name='Collection \xe9diteur', blank=True)),
                ('booklet_author', models.CharField(default=b'', help_text="Nom de l'auteur", max_length=255, verbose_name='Auteur de la note \xe9dit\xe9e', blank=True)),
                ('metadata_author', models.CharField(default=b'', help_text='R\xe9dacteur ; r\xe9dacteur', max_length=255, verbose_name='R\xe9dacteur(s) fiches ou registre', blank=True)),
                ('code', models.CharField(max_length=255, verbose_name='cote', validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}$', message=b'Code must conform to XXXX_XXX_000X_0000', code=b'invalid_code')])),
                ('code_partner', models.CharField(max_length=255, null=True, verbose_name="Cote dans l'institution partenaire", blank=True)),
                ('booklet_description', models.TextField(null=True, verbose_name='Documentation associ\xe9e', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='commentaires', blank=True)),
                ('physical_items_num', models.IntegerField(null=True, verbose_name='Nombre de composants (support / pi\xe8ce)', blank=True)),
                ('auto_period_access', models.BooleanField(default=True, verbose_name='Acc\xe8s automatique apr\xe8s la date glissante')),
            ],
            options={
                'ordering': ['code', 'title'],
                'db_table': 'int_collection',
                'verbose_name_plural': 'collections',
            },
        ),
        migrations.CreateModel(
            name='CollectionCollectors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection')),
                ('collector', models.ForeignKey(verbose_name='collector', to='telemeta_api.Authority')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_collector',
                'verbose_name_plural': 'collection_collectors',
            },
        ),
        migrations.CreateModel(
            name='CollectionInformer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection')),
                ('informer', models.ForeignKey(verbose_name='informer', to='telemeta_api.Authority')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_informer',
                'verbose_name_plural': 'collection_informers',
            },
        ),
        migrations.CreateModel(
            name='CollectionLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_collection_language',
                'verbose_name_plural': 'collection_languages',
            },
        ),
        migrations.CreateModel(
            name='CollectionLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_location',
                'verbose_name_plural': 'collection_locations',
            },
        ),
        migrations.CreateModel(
            name='CollectionPublisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_publisher',
                'verbose_name_plural': 'collection_publishers',
            },
        ),
        migrations.CreateModel(
            name='Coupe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_coupe',
                'verbose_name_plural': 'coupes',
            },
        ),
        migrations.CreateModel(
            name='Dance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_dance',
                'verbose_name_plural': 'dances',
            },
        ),
        migrations.CreateModel(
            name='DomainMusic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_domain_music',
                'verbose_name_plural': 'domain_musics',
            },
        ),
        migrations.CreateModel(
            name='DomainSong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_domain_song',
                'verbose_name_plural': 'domain_songs',
            },
        ),
        migrations.CreateModel(
            name='DomainTale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_domain_tale',
                'verbose_name_plural': 'domain_tales',
            },
        ),
        migrations.CreateModel(
            name='DomainVocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_domain_vocal',
                'verbose_name_plural': 'domain_vocals',
            },
        ),
        migrations.CreateModel(
            name='EmitVox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name="Nature de l'\xe9mission vocale")),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': [],
                'db_table': 'emit_vox',
                'verbose_name_plural': 'nature des emissions vocales',
            },
        ),
        migrations.CreateModel(
            name='ExtMediaItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mshs_alt_title', models.CharField(max_length=255, verbose_name='alternate title', blank=True)),
                ('description', models.TextField(help_text='Describe the item', verbose_name='description', blank=True)),
                ('mshs_timbre', models.CharField(max_length=255, verbose_name="Timbre de l'air", blank=True)),
                ('mshs_timbre_ref', models.CharField(max_length=1024, verbose_name='Timbre(s) r\xe9f\xe9renc\xe9(s)', blank=True)),
                ('mshs_timbre_code', models.CharField(max_length=255, verbose_name='Cote du timbre', blank=True)),
                ('mshs_melody', models.TextField(help_text='You can use ABC notation', verbose_name='M\xe9lodie (transcription alphab\xe9tique)', blank=True)),
                ('mshs_domain', models.CharField(blank=True, max_length=5, verbose_name='Domain', choices=[(b'T', b'T\xc3\xa9moignage'), (b'C', b'Chanson'), (b'A', b'Autre expression vocale'), (b'I', b'Expression instrumentale'), (b'R', b'Conte ou r\xc3\xa9cit l\xc3\xa9gendaire')])),
                ('mshs_domain_song', models.CharField(max_length=255, verbose_name='kind of song', blank=True)),
                ('mshs_domain_vocal', models.CharField(max_length=255, verbose_name='Autre expression vocale', blank=True)),
                ('mshs_domain_music', models.CharField(max_length=255, verbose_name='Expression instrumentale', blank=True)),
                ('mshs_domain_tale', models.CharField(max_length=255, verbose_name='Conte', blank=True)),
                ('mshs_details', models.TextField(verbose_name="Pr\xe9cisions sur l'item", blank=True)),
                ('mshs_function', models.CharField(max_length=255, verbose_name='Fonction(s)', blank=True)),
                ('mshs_dance', models.CharField(max_length=255, verbose_name='Danse(s)', blank=True)),
                ('mshs_dance_details', models.TextField(verbose_name='Pr\xe9cisions sur la danse', blank=True)),
                ('mshs_deposit_digest', models.TextField(verbose_name='R\xe9sum\xe9', blank=True)),
                ('mshs_deposit_thematic', models.TextField(verbose_name='Th\xe9matiques', blank=True)),
                ('mshs_deposit_names', models.TextField(help_text='First name, Last name ; First name, Last name', verbose_name='Nom(s) propre(s) cit\xe9(s) ', blank=True)),
                ('mshs_deposit_places', models.TextField(help_text='Place named; place named; ...', verbose_name='Lieu(x) cit\xe9(s)', blank=True)),
                ('mshs_deposit_periods', models.TextField(help_text='Period recounted; period recounted; ...', verbose_name='P\xe9riode(s) cit\xe9e(s)', blank=True)),
                ('mshs_text_bool', models.BooleanField(default=False, verbose_name='Text ?')),
                ('mshs_text', models.TextField(verbose_name='Text', blank=True)),
                ('mshs_incipit', models.TextField(verbose_name='incipit', blank=True)),
                ('mshs_refrain', models.TextField(verbose_name='refrain', blank=True)),
                ('mshs_jingle', models.TextField(verbose_name='jingle', blank=True)),
                ('mshs_title_ref_coirault', models.CharField(max_length=255, verbose_name='Title ref. Coirault', blank=True)),
                ('mshs_code_coirault', models.CharField(max_length=255, verbose_name='code Coirault', blank=True)),
                ('mshs_title_ref_laforte', models.CharField(max_length=255, verbose_name='Title ref. Laforte', blank=True)),
                ('mshs_code_laforte', models.CharField(max_length=255, verbose_name='code Laforte', blank=True)),
                ('mshs_title_ref_Dela', models.CharField(max_length=255, verbose_name='Title ref. Delarue-Teneze', blank=True)),
                ('mshs_code_Dela', models.CharField(max_length=255, verbose_name='code Delarue-Teneze', blank=True)),
                ('mshs_title_ref_Aare', models.CharField(max_length=255, verbose_name='Title ref. Aare-Thomson', blank=True)),
                ('mshs_code_Aare', models.CharField(max_length=255, verbose_name='code Aare-Thomson', blank=True)),
                ('mshs_musical_organization', models.CharField(max_length=255, verbose_name='Organisation musicale', blank=True)),
                ('mshs_group', models.CharField(max_length=255, verbose_name='Formation', blank=True)),
                ('code', models.CharField(default=telemeta_mshs.apps.telemeta_api.models.ext_media_item.default_code, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}_[0-9]{3}$', message=b'Code must conform to XXXX_XXX_000X_0000_000', code=b'invalid_code')], max_length=255, blank=True, help_text='CollectionCode_ItemCode', unique=True, verbose_name='code')),
                ('media_item', models.OneToOneField(to='telemeta.MediaItem')),
                ('mshs_ch_coupe', models.ForeignKey(verbose_name='coupe', blank=True, to='telemeta_api.Coupe', null=True)),
            ],
            options={
                'db_table': 'ext_media_item',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Fond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='titre')),
                ('alt_title', models.CharField(max_length=255, verbose_name='Titre original', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('code', models.CharField(max_length=255, verbose_name='cote', validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}$', message=b'Code must conform to XXXX_XXX', code=b'invalid_code')])),
                ('code_partner', models.CharField(max_length=255, null=True, verbose_name="Cote dans l'institution partenaire", blank=True)),
                ('conservation_site', models.CharField(max_length=255, null=True, verbose_name='lieu de conservation original', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='commentaires', blank=True)),
                ('acquisition_mode', models.ForeignKey(related_name='fonds', on_delete=django.db.models.deletion.SET_NULL, verbose_name="Mode d'acquisition", blank=True, to='telemeta_api.AcquisitionMode', null=True)),
            ],
            options={
                'ordering': ['code', 'title'],
                'db_table': 'fond',
                'verbose_name_plural': 'fonds',
            },
        ),
        migrations.CreateModel(
            name='HornbostelSachs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(unique=True, max_length=30, verbose_name='Num\xe9rotation')),
                ('name', models.TextField(null=True, verbose_name='Nom', blank=True)),
            ],
            options={
                'ordering': [],
                'db_table': 'hornbostelsachs',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('notes', models.TextField(null=True, verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'institutions',
                'verbose_name_plural': 'institutions',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
                ('typology', models.ForeignKey(verbose_name='HornbostelSachs', blank=True, to='telemeta_api.HornbostelSachs', null=True)),
            ],
            options={
                'ordering': [],
                'db_table': 'instrument',
                'verbose_name_plural': 'instruments',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='titre')),
                ('alt_title', models.CharField(default=b'', max_length=255, verbose_name='autre titre', blank=True)),
                ('trans_title', models.CharField(default=b'', max_length=255, verbose_name='traduction titre', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('code', models.CharField(max_length=255, verbose_name='cote', validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}_[0-9]{3}$', message=b'Code must conform to XXXX_XXX_000X_0000_000', code=b'invalid_code')])),
                ('code_partner', models.CharField(max_length=255, null=True, verbose_name="cote de l'item dans l'institution partenaire", blank=True)),
                ('auto_period_access', models.BooleanField(default=True, verbose_name='acc\xe8s automatique apr\xe8s la date glissante')),
                ('remarks', models.TextField(null=True, verbose_name="remarques concernant les donn\xe9es d'archivage", blank=True)),
                ('date_edit', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('approx_duration', models.DurationField(null=True, verbose_name='dur\xe9e estim\xe9e', blank=True)),
                ('file', models.FileField(upload_to=b'items/%Y/%m/%d', max_length=1024, verbose_name='fichier son', db_column=b'filename')),
                ('timbre', models.TextField(null=True, verbose_name="Timbre de l'air", blank=True)),
                ('timbre_ref', models.TextField(null=True, verbose_name='Timbre r\xe9f\xe9renc\xe9', blank=True)),
                ('melody', models.TextField(help_text='Vous pouvez utiliser la notation ABC', null=True, verbose_name='M\xe9lodie (transcription alphab\xe9tique)', blank=True)),
                ('domain', models.CharField(blank=True, max_length=5, verbose_name='Domaine', choices=[(b'T', b'T\xc3\xa9moignage'), (b'C', b'Chanson'), (b'A', b'Autre expression vocale'), (b'I', b'Expression instrumentale'), (b'R', b'Conte ou r\xc3\xa9cit l\xc3\xa9gendaire')])),
                ('deposit_digest', models.TextField(null=True, verbose_name='R\xe9sum\xe9', blank=True)),
                ('deposit_names', models.TextField(help_text='First name, Last name ; First name, Last name', null=True, verbose_name='Nom(s) propre(s) cit\xe9(s) ', blank=True)),
                ('deposit_places', models.TextField(help_text='Place named; place named; ...', null=True, verbose_name='Lieu(x) cit\xe9(s)', blank=True)),
                ('deposit_periods', models.TextField(help_text='Period recounted; period recounted; ...', null=True, verbose_name='P\xe9riode(s) cit\xe9e(s)', blank=True)),
                ('text_bool', models.BooleanField(default=False, verbose_name='Text ?')),
                ('text', models.TextField(null=True, verbose_name='Text', blank=True)),
                ('incipit', models.TextField(null=True, verbose_name='incipit', blank=True)),
                ('refrain', models.TextField(null=True, verbose_name='refrain', blank=True)),
                ('jingle', models.TextField(null=True, verbose_name='jingle', blank=True)),
                ('collection', models.ForeignKey(related_name='collection', verbose_name='Collection', to='telemeta_api.Collection')),
                ('coupe', models.ForeignKey(related_name='items', on_delete=django.db.models.deletion.SET_NULL, verbose_name='coupe', blank=True, to='telemeta_api.Coupe', null=True)),
            ],
            options={
                'ordering': ['code', 'title'],
                'db_table': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='ItemAnalysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element_type', models.CharField(default=b'analysis', max_length=255, verbose_name='type element')),
                ('analyzer_id', models.CharField(default=b'', max_length=255, verbose_name='id', blank=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='nom', blank=True)),
                ('value', models.CharField(default=b'', max_length=255, verbose_name='valeur', blank=True)),
                ('unit', models.CharField(default=b'', max_length=255, verbose_name='unit\xe9', blank=True)),
                ('item', models.ForeignKey(related_name='analysis', verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_analysis',
                'verbose_name_plural': 'item_analysises',
            },
        ),
        migrations.CreateModel(
            name='ItemAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.ForeignKey(verbose_name='author', to='telemeta_api.Authority')),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_author',
                'verbose_name_plural': 'item_authors',
            },
        ),
        migrations.CreateModel(
            name='ItemCoirault',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_coirault',
                'verbose_name_plural': 'item_coiraults',
            },
        ),
        migrations.CreateModel(
            name='ItemCollector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collector', models.ForeignKey(verbose_name='collector', to='telemeta_api.Authority')),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_collector',
                'verbose_name_plural': 'item_collectors',
            },
        ),
        migrations.CreateModel(
            name='ItemCompositor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compositor', models.ForeignKey(verbose_name='XXXXXX', to='telemeta_api.Authority')),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_compositor',
                'verbose_name_plural': 'item_compositors',
            },
        ),
        migrations.CreateModel(
            name='ItemDance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dance', models.ForeignKey(verbose_name='Fonction', to='telemeta_api.Dance')),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_dance',
                'verbose_name_plural': 'item_dances',
            },
        ),
        migrations.CreateModel(
            name='ItemDomainMusic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_music', models.ForeignKey(verbose_name="Genre de l'expression instrumentale", to='telemeta_api.DomainMusic')),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_domain_music',
                'verbose_name_plural': 'item_domain_musics',
            },
        ),
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
        migrations.CreateModel(
            name='ItemDomainTale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_tale', models.ForeignKey(verbose_name='Genre du conte', to='telemeta_api.DomainTale')),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_domain_tale',
                'verbose_name_plural': 'item_domain_tales',
            },
        ),
        migrations.CreateModel(
            name='ItemDomainVocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_vocal', models.ForeignKey(verbose_name="Genre de l'autre expression vocale", to='telemeta_api.DomainVocal')),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_domain_vocal',
                'verbose_name_plural': 'item_domain_vocals',
            },
        ),
        migrations.CreateModel(
            name='ItemInformer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('informer', models.ForeignKey(verbose_name='XXXXXX', to='telemeta_api.Authority')),
                ('item', models.ForeignKey(verbose_name='XXXXXX', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_informer',
                'verbose_name_plural': 'item_informers',
            },
        ),
        migrations.CreateModel(
            name='ItemLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='item', to='telemeta_api.Item')),
            ],
            options={
                'db_table': 'api_item_language',
                'verbose_name_plural': 'item_languages',
            },
        ),
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
        migrations.CreateModel(
            name='ItemMusicalGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_musical_group',
                'verbose_name_plural': 'item_musical_groups',
            },
        ),
        migrations.CreateModel(
            name='ItemMusicalOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_musical_organization',
                'verbose_name_plural': 'item_musical_organizations',
            },
        ),
        migrations.CreateModel(
            name='ItemThematic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_thematic',
                'verbose_name_plural': 'item_thematics',
            },
        ),
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
        migrations.CreateModel(
            name='ItemUsefulness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(verbose_name='Item', to='telemeta_api.Item')),
            ],
            options={
                'ordering': [],
                'db_table': 'api_item_usefulness',
                'verbose_name_plural': 'item_usefulnesses',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=3, verbose_name='identifier')),
                ('part2B', models.CharField(max_length=3, verbose_name='equivalent ISO 639-2 identifier (bibliographic)')),
                ('part2T', models.CharField(max_length=3, verbose_name='equivalent ISO 639-2 identifier (terminologic)')),
                ('part1', models.CharField(max_length=1, verbose_name='equivalent ISO 639-1 identifier')),
                ('scope', models.CharField(max_length=1, verbose_name='scope', choices=[(b'I', b'Individual'), (b'M', b'Macrolanguage'), (b'S', b'Special')])),
                ('type', models.CharField(max_length=1, verbose_name='type', choices=[(b'A', b'Ancient'), (b'C', b'Constructed'), (b'E', b'Extinct'), (b'H', b'Historical'), (b'L', b'Living'), (b'S', b'Special')])),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('comment', models.TextField(null=True, verbose_name='comment', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='LegalRights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_legal_rights',
                'verbose_name_plural': 'legal rights',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255, verbose_name='code')),
                ('name', models.CharField(max_length=1024, verbose_name='name')),
                ('notes', models.TextField(null=True, verbose_name='notes', blank=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_media_type',
                'verbose_name_plural': 'media types',
            },
        ),
        migrations.CreateModel(
            name='MetadataAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_metadata_author',
                'verbose_name_plural': 'metadata authors',
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='titre')),
                ('alt_title', models.CharField(max_length=255, verbose_name='Titre original', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('code', models.CharField(max_length=255, verbose_name='cote', validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}$', message=b'Code must conform to XXXX_XXX_000X', code=b'invalid_code')])),
                ('code_partner', models.CharField(max_length=255, null=True, verbose_name="Cote de la mission dans l'institution partenaire", blank=True)),
                ('fonds', models.ForeignKey(related_name='mission', verbose_name='Fonds', to='telemeta_api.Fond')),
            ],
            options={
                'ordering': ['code', 'title'],
                'db_table': 'mission',
                'verbose_name_plural': 'missions',
            },
        ),
        migrations.CreateModel(
            name='MusicalGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_musical_group',
                'verbose_name_plural': 'musical_groups',
            },
        ),
        migrations.CreateModel(
            name='MusicalOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_musical_organization',
                'verbose_name_plural': 'musical_organizations',
            },
        ),
        migrations.CreateModel(
            name='PerformanceCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name='Nombre')),
                ('collection', models.ForeignKey(verbose_name='collection', to='telemeta_api.Collection')),
                ('emit', models.ForeignKey(verbose_name="Nature de l'\xe9mission vocale", blank=True, to='telemeta_api.EmitVox', null=True)),
                ('instrument', models.ForeignKey(verbose_name='instrument', blank=True, to='telemeta_api.Instrument', null=True)),
            ],
            options={
                'ordering': [],
                'db_table': 'performance_collection',
                'verbose_name_plural': 'interpretes',
            },
        ),
        migrations.CreateModel(
            name='PerformanceCollectionMusician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('musician', models.ForeignKey(verbose_name='musician', to='telemeta_api.Authority')),
                ('performance_collection', models.ForeignKey(verbose_name='performance', to='telemeta_api.PerformanceCollection')),
            ],
            options={
                'ordering': [],
                'db_table': 'performance_collection_musician',
                'verbose_name_plural': 'musicians',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_publisher',
                'verbose_name_plural': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='RecordingContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_recording_context',
                'verbose_name_plural': 'recording contexts',
            },
        ),
        migrations.CreateModel(
            name='SkosCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='nom')),
                ('uri', models.CharField(max_length=500, verbose_name='uri')),
                ('number', models.CharField(max_length=40, verbose_name='num\xe9rotation')),
                ('type', models.CharField(max_length=40, verbose_name='type')),
                ('collection', models.ForeignKey(related_name='skos_collection', default=None, blank=True, to='telemeta_api.SkosCollection', null=True, verbose_name='Collection parente')),
            ],
            options={
                'ordering': [],
                'db_table': 'skos_collection',
                'verbose_name_plural': 'skos_collections',
            },
        ),
        migrations.CreateModel(
            name='SkosConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='nom')),
                ('uri', models.CharField(max_length=500, verbose_name='uri')),
                ('number', models.CharField(max_length=40, verbose_name='num\xe9rotation')),
                ('abstract', models.TextField(null=True, blank=True)),
                ('collection', models.ForeignKey(related_name='skos_concept', default=None, verbose_name='Collection parente', to='telemeta_api.SkosCollection')),
            ],
            options={
                'ordering': ['number'],
                'db_table': 'skos_concept',
                'verbose_name_plural': 'skos_concepts',
            },
        ),
        migrations.CreateModel(
            name='Thematic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_thematic',
                'verbose_name_plural': 'thematics',
            },
        ),
        migrations.CreateModel(
            name='Usefulness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Nom')),
                ('notes', models.TextField(null=True, verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_usefulness',
                'verbose_name_plural': 'usefulnesses',
            },
        ),
        migrations.AddField(
            model_name='itemusefulness',
            name='usefulness',
            field=models.ForeignKey(verbose_name='Fonction', to='telemeta_api.Usefulness'),
        ),
        migrations.AddField(
            model_name='itemthematic',
            name='thematic',
            field=models.ForeignKey(verbose_name='Fonction', to='telemeta_api.Thematic'),
        ),
        migrations.AddField(
            model_name='itemmusicalorganization',
            name='musical_organization',
            field=models.ForeignKey(verbose_name='Fonction', to='telemeta_api.MusicalOrganization'),
        ),
        migrations.AddField(
            model_name='itemmusicalgroup',
            name='musical_group',
            field=models.ForeignKey(verbose_name='Fonction', to='telemeta_api.MusicalGroup'),
        ),
        migrations.AddField(
            model_name='itemlanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='language', to='telemeta_api.Language'),
        ),
        migrations.AddField(
            model_name='itemcoirault',
            name='coirault',
            field=models.ForeignKey(verbose_name='Coirault', to='telemeta_api.SkosConcept'),
        ),
        migrations.AddField(
            model_name='itemcoirault',
            name='item',
            field=models.ForeignKey(verbose_name='item', to='telemeta_api.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='media_type',
            field=models.ForeignKey(related_name='items', on_delete=django.db.models.deletion.SET_NULL, verbose_name='type de media', blank=True, to='telemeta_api.MediaType', null=True),
        ),
        migrations.AddField(
            model_name='fond',
            name='institution',
            field=models.ForeignKey(related_name='fonds', verbose_name='Institution', to='telemeta_api.Institution'),
        ),
        migrations.AddField(
            model_name='collectionpublisher',
            name='publisher',
            field=models.ForeignKey(verbose_name='publisher', to='telemeta_api.Publisher'),
        ),
        migrations.AddField(
            model_name='collectionlocation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='location', to='telemeta_api.Location'),
        ),
        migrations.AddField(
            model_name='collectionlanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='language', to='telemeta_api.Language'),
        ),
        migrations.AddField(
            model_name='collection',
            name='legal_rights',
            field=models.ForeignKey(related_name='collection', on_delete=django.db.models.deletion.SET_NULL, verbose_name="Droits d'utilisation", blank=True, to='telemeta_api.LegalRights', null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='media_type',
            field=models.ForeignKey(related_name='collection', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Type de m\xe9dia', blank=True, to='telemeta_api.MediaType', null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='mission',
            field=models.ForeignKey(related_name='collection', default=b'', verbose_name='Mission', blank=True, to='telemeta_api.Mission'),
        ),
        migrations.AddField(
            model_name='authority',
            name='birth_location',
            field=models.ForeignKey(related_name='birth_location', on_delete=django.db.models.deletion.SET_NULL, verbose_name='birth location', blank=True, to='telemeta_api.Location', null=True),
        ),
        migrations.AddField(
            model_name='authority',
            name='death_location',
            field=models.ForeignKey(related_name='death_location', on_delete=django.db.models.deletion.SET_NULL, verbose_name='death location', blank=True, to='telemeta_api.Location', null=True),
        ),
    ]
