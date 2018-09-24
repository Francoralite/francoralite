# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0011_collectionlanguage'),
    ]

    operations = [
        migrations.AddField(
            model_name='extmediaitem',
            name='code',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}_[0-9]{3}$', message=b'Code must conform to XXXX_XXX_000X_0000_000', code=b'invalid_code')], max_length=255, blank=True, help_text='CollectionCode_ItemCode', unique=True, verbose_name='code'),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='description',
            field=models.TextField(help_text='Describe the item', verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_alt_title',
            field=models.CharField(max_length=255, verbose_name='alternate title', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_code_Aare',
            field=models.CharField(max_length=255, verbose_name='code Aare-Thomson', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_code_Dela',
            field=models.CharField(max_length=255, verbose_name='code Delarue-Teneze', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_code_coirault',
            field=models.CharField(max_length=255, verbose_name='code Coirault', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_code_laforte',
            field=models.CharField(max_length=255, verbose_name='code Laforte', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_dance',
            field=models.CharField(max_length=255, verbose_name='Danse(s)', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_dance_details',
            field=models.TextField(verbose_name='Pr\xe9cisions sur la danse', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_deposit_digest',
            field=models.TextField(verbose_name='R\xe9sum\xe9', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_deposit_names',
            field=models.TextField(help_text='First name, Last name ; First name, Last name', verbose_name='Nom(s) propre(s) cit\xe9(s) ', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_deposit_periods',
            field=models.TextField(help_text='Period recounted; period recounted; ...', verbose_name='P\xe9riode(s) cit\xe9e(s)', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_deposit_places',
            field=models.TextField(help_text='Place named; place named; ...', verbose_name='Lieu(x) cit\xe9(s)', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_deposit_thematic',
            field=models.TextField(verbose_name='Th\xe9matiques', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_details',
            field=models.TextField(verbose_name="Pr\xe9cisions sur l'item", blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_domain',
            field=models.CharField(blank=True, max_length=5, verbose_name='Domain', choices=[(b'T', b'T\xc3\xa9moignage'), (b'C', b'Chanson'), (b'A', b'Autre expression vocale'), (b'I', b'Expression instrumentale'), (b'R', b'Conte ou r\xc3\xa9cit l\xc3\xa9gendaire')]),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_domain_music',
            field=models.CharField(max_length=255, verbose_name='Expression instrumentale', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_domain_song',
            field=models.CharField(max_length=255, verbose_name='kind of song', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_domain_tale',
            field=models.CharField(max_length=255, verbose_name='Conte', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_domain_vocal',
            field=models.CharField(max_length=255, verbose_name='Autre expression vocale', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_function',
            field=models.CharField(max_length=255, verbose_name='Fonction(s)', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_group',
            field=models.CharField(max_length=255, verbose_name='Formation', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_incipit',
            field=models.TextField(verbose_name='incipit', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_jingle',
            field=models.TextField(verbose_name='jingle', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_melody',
            field=models.TextField(help_text='You can use ABC notation', verbose_name='M\xe9lodie (transcription alphab\xe9tique)', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_musical_organization',
            field=models.CharField(max_length=255, verbose_name='Organisation musicale', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_refrain',
            field=models.TextField(verbose_name='refrain', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_text',
            field=models.TextField(verbose_name='Text', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_text_bool',
            field=models.BooleanField(default=False, verbose_name='Text ?'),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_timbre',
            field=models.CharField(max_length=255, verbose_name="Timbre de l'air", blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_timbre_code',
            field=models.CharField(max_length=255, verbose_name='Cote du timbre', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_timbre_ref',
            field=models.CharField(max_length=1024, verbose_name='Timbre(s) r\xe9f\xe9renc\xe9(s)', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_title_ref_Aare',
            field=models.CharField(max_length=255, verbose_name='Title ref. Aare-Thomson', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_title_ref_Dela',
            field=models.CharField(max_length=255, verbose_name='Title ref. Delarue-Teneze', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_title_ref_coirault',
            field=models.CharField(max_length=255, verbose_name='Title ref. Coirault', blank=True),
        ),
        migrations.AddField(
            model_name='extmediaitem',
            name='mshs_title_ref_laforte',
            field=models.CharField(max_length=255, verbose_name='Title ref. Laforte', blank=True),
        ),
    ]
