# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0002_document_documentcollection_documentitem_documentmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFond',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='telemeta_api.Document', on_delete=models.CASCADE)),
                ('fond', models.ForeignKey(related_name='related_document', verbose_name='fond', to='telemeta_api.Fond', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['fond', 'title'],
                'db_table': 'api_document_fond',
                'verbose_name_plural': 'document',
            },
            bases=('telemeta_api.document',),
        ),
    ]
