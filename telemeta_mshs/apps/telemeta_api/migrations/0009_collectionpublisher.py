# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0006_enumerationproperty'),
        ('telemeta_api', '0008_collectioninformer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPublisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta.MediaCollection')),
                ('publisher', telemeta.models.fields.ForeignKey(verbose_name='publisher', to='telemeta_api.Authority')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_publisher',
                'verbose_name_plural': 'collection_publishers',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
