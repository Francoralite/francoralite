# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0066_auto_20190812_1035'),
    ]

    operations = [
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
                ('comment', models.TextField(verbose_name='comment')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'api_language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.AlterField(
            model_name='collectionlanguage',
            name='language',
            field=telemeta.models.fields.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='language', to='telemeta_api.Language'),
        ),
        migrations.AddField(
            model_name='itemlanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='language', to='telemeta_api.Language'),
        ),
    ]
