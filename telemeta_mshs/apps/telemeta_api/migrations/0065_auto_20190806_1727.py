# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0064_itemcoirault'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acquisitionmode',
            options={'ordering': ['name'], 'verbose_name_plural': 'acquisitions'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['code', 'title'], 'verbose_name_plural': 'collections'},
        ),
        migrations.AlterModelOptions(
            name='coupe',
            options={'ordering': ['name'], 'verbose_name_plural': 'coupes'},
        ),
        migrations.AlterModelOptions(
            name='legalrights',
            options={'ordering': ['name'], 'verbose_name_plural': 'legal rights'},
        ),
        migrations.AlterModelOptions(
            name='mediatype',
            options={'ordering': ['name'], 'verbose_name_plural': 'media types'},
        ),
        migrations.AlterModelOptions(
            name='metadataauthor',
            options={'ordering': ['name'], 'verbose_name_plural': 'metadata authors'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name'], 'verbose_name_plural': 'publishers'},
        ),
        migrations.AlterModelOptions(
            name='recordingcontext',
            options={'ordering': ['name'], 'verbose_name_plural': 'recording contexts'},
        ),
        migrations.RemoveField(
            model_name='acquisitionmode',
            name='value',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='public_access',
        ),
        migrations.RemoveField(
            model_name='coupe',
            name='value',
        ),
        migrations.RemoveField(
            model_name='legalrights',
            name='value',
        ),
        migrations.RemoveField(
            model_name='mediatype',
            name='value',
        ),
        migrations.RemoveField(
            model_name='metadataauthor',
            name='value',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='value',
        ),
        migrations.RemoveField(
            model_name='recordingcontext',
            name='value',
        ),
        migrations.AddField(
            model_name='acquisitionmode',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 8, 6, 17, 26, 50, 731017), unique=True, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupe',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 8, 6, 17, 27, 2, 228901), unique=True, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='legalrights',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 8, 6, 17, 27, 8, 621821), unique=True, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mediatype',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 8, 6, 17, 27, 12, 614349), unique=True, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadataauthor',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 8, 6, 17, 27, 17, 446800), unique=True, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publisher',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 8, 6, 17, 27, 25, 288528), unique=True, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recordingcontext',
            name='name',
            field=models.CharField(default=datetime.datetime(2019, 8, 6, 17, 27, 33, 953846), unique=True, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acquisitionmode',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='code',
            field=models.CharField(max_length=255, verbose_name='cote', validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}$', message=b'Code must conform to XXXX_XXX_000X_0000', code=b'invalid_code')]),
        ),
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(max_length=255, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='coupe',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='legalrights',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='mediatype',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='metadataauthor',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='recordingcontext',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterModelTable(
            name='acquisitionmode',
            table='api_acquisition',
        ),
        migrations.AlterModelTable(
            name='coupe',
            table='api_coupe',
        ),
        migrations.AlterModelTable(
            name='mediatype',
            table='api_media_type',
        ),
        migrations.AlterModelTable(
            name='metadataauthor',
            table='api_metadata_author',
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='api_publisher',
        ),
        migrations.AlterModelTable(
            name='recordingcontext',
            table='api_recording_context',
        ),
    ]
