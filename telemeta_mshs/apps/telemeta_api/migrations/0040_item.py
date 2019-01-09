# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0039_domainsong'),
    ]

    operations = [
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
                ('media_type', models.ForeignKey(related_name='items', on_delete=django.db.models.deletion.SET_NULL, verbose_name='type de media', blank=True, to='telemeta_api.MediaType', null=True)),
            ],
            options={
                'ordering': ['code', 'title'],
                'db_table': 'item',
                'verbose_name_plural': 'items',
            },
        ),
    ]
