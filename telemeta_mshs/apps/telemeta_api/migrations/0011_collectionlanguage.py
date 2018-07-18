# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0006_enumerationproperty'),
        ('telemeta_api', '0010_collectionlocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta.MediaCollection')),
                ('language', telemeta.models.fields.ForeignKey(verbose_name='language', to='telemeta.Language')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_language',
                'verbose_name_plural': 'collection_languages',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
