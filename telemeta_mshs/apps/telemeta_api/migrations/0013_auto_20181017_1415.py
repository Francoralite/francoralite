# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta_mshs.apps.telemeta_api.models.ext_media_item
import telemeta.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0012_auto_20180723_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authority',
            name='civilite',
        ),
        migrations.RemoveField(
            model_name='authority',
            name='roles',
        ),
        migrations.AddField(
            model_name='authority',
            name='civility',
            field=telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='civility', blank=True),
        ),
        migrations.AddField(
            model_name='authority',
            name='is_author',
            field=telemeta.models.fields.BooleanField(default=False, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='authority',
            name='is_collector',
            field=telemeta.models.fields.BooleanField(default=False, verbose_name='collector'),
        ),
        migrations.AddField(
            model_name='authority',
            name='is_composer',
            field=telemeta.models.fields.BooleanField(default=False, verbose_name='composer'),
        ),
        migrations.AddField(
            model_name='authority',
            name='is_editor',
            field=telemeta.models.fields.BooleanField(default=False, verbose_name='editor'),
        ),
        migrations.AddField(
            model_name='authority',
            name='is_informer',
            field=telemeta.models.fields.BooleanField(default=False, verbose_name='informer'),
        ),
        migrations.AlterField(
            model_name='extmediaitem',
            name='code',
            field=models.CharField(default=telemeta_mshs.apps.telemeta_api.models.ext_media_item.default_code, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}_[0-9]{3}$', message=b'Code must conform to XXXX_XXX_000X_0000_000', code=b'invalid_code')], max_length=255, blank=True, help_text='CollectionCode_ItemCode', unique=True, verbose_name='code'),
        ),
    ]
