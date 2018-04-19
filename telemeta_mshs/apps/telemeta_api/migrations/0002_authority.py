# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import telemeta.models.fields
import dirtyfields.dirtyfields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0006_enumerationproperty'),
        ('telemeta_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='last name', blank=True)),
                ('first_name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='first name', blank=True)),
                ('civilite', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='civilite', blank=True)),
                ('alias', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='alias', blank=True)),
                ('roles', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Roles', blank=True, choices=[(b'ENQ', b'Enqu\xc3\xaateur'), (b'INF', b'Informateur'), (b'AUT', b'Auteur'), (b'CMP', b'Compositeur'), (b'EDT', b'Editeur')])),
                ('birth_date', telemeta.models.fields.DateField(default=None, null=True, blank=True)),
                ('death_date', telemeta.models.fields.DateField(default=None, null=True, blank=True)),
                ('biography', telemeta.models.fields.TextField(default=None, null=True, verbose_name='biography', blank=True)),
                ('uri', models.URLField(null=True, verbose_name='URI', blank=True)),
                ('birth_location', telemeta.models.fields.ForeignKey(related_name='birth_location', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='telemeta.Location', null=True, verbose_name='birth location')),
                ('death_location', telemeta.models.fields.ForeignKey(related_name='death_location', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='telemeta.Location', null=True, verbose_name='death location')),
            ],
            options={
                'ordering': [],
                'db_table': 'authority',
                'verbose_name_plural': 'authorities',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
    ]
