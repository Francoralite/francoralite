# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0005_extmediacollection'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionCollectors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.RemoveField(
            model_name='extmediacollection',
            name='collectors',
        ),
        migrations.RemoveField(
            model_name='extmediacollection',
            name='informers',
        ),
        migrations.RemoveField(
            model_name='extmediacollection',
            name='language_iso',
        ),
        migrations.RemoveField(
            model_name='extmediacollection',
            name='location',
        ),
        migrations.RemoveField(
            model_name='extmediacollection',
            name='publishers',
        ),
        migrations.AlterField(
            model_name='extmediacollection',
            name='cultural_area',
            field=models.TextField(default=b'', help_text=b'Aire culturelle ; Aire culturelle', verbose_name=b'cultural area', blank=True),
        ),
        migrations.AlterField(
            model_name='extmediacollection',
            name='language',
            field=models.TextField(default=b'', help_text=b'Langage ; langage', verbose_name=b'langage', blank=True),
        ),
        migrations.AddField(
            model_name='collectioncollectors',
            name='collection',
            field=telemeta.models.fields.ForeignKey(verbose_name='collection', to='telemeta_api.ExtMediaCollection'),
        ),
        migrations.AddField(
            model_name='collectioncollectors',
            name='collector',
            field=telemeta.models.fields.ForeignKey(verbose_name='collector', to='telemeta_api.Authority'),
        ),
    ]
