# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0006_enumerationproperty'),
        ('telemeta_api', '0007_auto_20180712_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionInformer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta.MediaCollection')),
                ('informer', telemeta.models.fields.ForeignKey(verbose_name='informer', to='telemeta_api.Authority')),
            ],
            options={
                'ordering': [],
                'db_table': 'collection_informer',
                'verbose_name_plural': 'collection_informers',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
