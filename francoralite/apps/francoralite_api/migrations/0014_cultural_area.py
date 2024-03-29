# Generated by Django 3.1.14 on 2024-01-25 15:37

from django.db import migrations, models
import django.db.models.deletion


def create_cultural_areas(apps, schema_editor):
    CollectionCulturalArea = apps.get_model('francoralite_api', 'CollectionCulturalArea')
    Collection = apps.get_model('francoralite_api', 'Collection')
    CulturalArea = apps.get_model('francoralite_api', 'CulturalArea')

    cultural_areas_ids = {}

    qs = Collection.objects.values_list('id', 'cultural_area')
    qs = qs.exclude(cultural_area=None).exclude(cultural_area='')
    for collection_id, cultural_area_name in qs:
        cultural_area_id = cultural_areas_ids.get(cultural_area_name)

        if not cultural_area_id:
            cultural_area_id = CulturalArea.objects.get_or_create(name=cultural_area_name)[0].id
            cultural_areas_ids[cultural_area_name] = cultural_area_id

        CollectionCulturalArea.objects.create(
            collection_id=collection_id,
            cultural_area_id=cultural_area_id,
        )


def reverse_cultural_areas(apps, schema_editor):
    CollectionCulturalArea = apps.get_model('francoralite_api', 'CollectionCulturalArea')
    Collection = apps.get_model('francoralite_api', 'Collection')

    qs = CollectionCulturalArea.objects.values_list('collection_id', 'cultural_area__name')
    for collection_id, cultural_area_name in qs:
        Collection.objects.filter(id=collection_id).update(cultural_area=cultural_area_name)


class Migration(migrations.Migration):

    dependencies = [
        ('francoralite_api', '0013_authoritycivility_civility'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('geojson', models.JSONField(blank=True, null=True, verbose_name='GeoJSON')),
            ],
            options={
                'verbose_name': 'aire culturelle',
                'verbose_name_plural': 'aires culturelles',
                'db_table': 'api_cultural_area',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CollectionCulturalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='francoralite_api.collection', verbose_name='collection')),
                ('cultural_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='francoralite_api.culturalarea', verbose_name='cultural area')),
            ],
            options={
                'verbose_name': 'cultural area of a collection',
                'verbose_name_plural': 'cultural areas of collections',
                'db_table': 'collection_cultural_area',
                'ordering': [],
                'unique_together': {('collection', 'cultural_area')},
            },
        ),
        migrations.RunPython(
            code=create_cultural_areas,
            reverse_code=reverse_cultural_areas,
            atomic=True,
        ),
        migrations.RemoveField(
            model_name='collection',
            name='cultural_area',
        ),
    ]
