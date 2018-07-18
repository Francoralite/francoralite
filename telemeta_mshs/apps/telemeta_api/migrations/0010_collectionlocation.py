# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0006_enumerationproperty'),
        ('telemeta_api', '0009_collectionpublisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta.MediaCollection')),
                ('location', telemeta.models.fields.ForeignKey(verbose_name='location', to='telemeta.Location')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_location',
                'verbose_name_plural': 'collection_locations',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
