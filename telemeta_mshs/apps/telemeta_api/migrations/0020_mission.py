# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.resource
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta_api', '0019_auto_20181026_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.CharField(max_length=250, null=True, verbose_name='description_old', blank=True)),
                ('descriptions', models.TextField(verbose_name='description', blank=True)),
                ('code', models.CharField(unique=True, max_length=250, verbose_name='code', validators=[telemeta.models.resource.is_valid_resource_code])),
                ('public_access', models.CharField(default=b'metadata', max_length=16, verbose_name='public access', choices=[(b'none', 'none'), (b'metadata', 'metadata'), (b'mixed', 'mixed'), (b'full', 'full')])),
                ('code_partner', models.CharField(max_length=4, null=True, verbose_name="Cote de la mission dans l'institution partenaire", blank=True)),
                ('fonds', models.ForeignKey(related_name='mission', verbose_name='Fonds', to='telemeta_api.Fond')),
            ],
            options={
                'ordering': [],
                'db_table': 'mission',
                'verbose_name_plural': 'missions',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
