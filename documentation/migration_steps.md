# Processus de migration vers Python3 / Django3

## Actions post migrations

* Renommer la table `telemeta_api_location`

    ```
    RENAME TABLE telemeta_api_location TO francoralite_api_location;
    ```

## Référencement des applications à supprimer

'bootstrap3',
'timezones',
'telemeta',
'timeside.player',
# 'timeside.server',
'sorl.thumbnail',
'jqchat',
'haystack',
# 'ipauth',
'suit',
'saved_searches',



# A verifier
'jsonrpc',
'extra_views',



# A garder
'django.contrib.auth',
'mozilla_django_oidc',  # Load after auth
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'django.contrib.admin',
'django.contrib.staticfiles',
'django_extensions',
'registration',
'rest_framework',
'rest_framework_xml',
'djcelery',
'djangobower', # A verifier
'django',
'rest_framework_swagger',
'django_filters',
'telemeta_mshs.apps.telemeta_api',
'telemeta_mshs.apps.telemeta_front',
'django_select2',
'leaflet',
'markdownx',
'corsheaders',
'debug_toolbar',
'rdflib',


## Suppression de Telemeta

### Référencement des tables rattachées à Telemeta

* acquisition_modes
* ad_conversions
* context_keywords
* copy_type
* ethnic_group_aliases
* ethnic_groups
* generic_styles
* identifier_type
* instrument_alias_relations
* instrument_aliases
* instrument_relations
* instruments
* languages
* legal_rights
* location_aliases
* location_relations
* location_types
* locations
* media_analysis
* media_collection_identifier
* media_collection_related
* media_collections
* media_corpus
* media_corpus_related
* media_fonds
* media_fonds_related
* media_formats
* media_item_identifier
* media_item_keywords
* media_item_performances
* media_item_related
* media_items
* media_markers
* media_parts
* media_status
* media_transcoding
* media_type
* metadata_authors
* metadata_writers
* organization
* original_channel_number
* original_format
* physical_formats
* playlist_resources
* playlists
* profiles
* publisher_collections
* publishers
* publishing_status
* recording_contexts
* revisions
* rights
* search_criteria
* searches
* tape_length
* tape_speed
* tape_vendor
* tape_wheel_diameter
* tape_width
* telemeta_enumerationproperty
* telemeta_media_transcoded
* topic
* vernacular_styles

### Vérification des données contenues dans ces tables

1. Création d'un script pour récupérer le nombre d'entrées dans ces tables
2. Validation que ces données n'étaient plus utilisées et ne devaient pas être migrées

Le script est `scripts/check_telemeta_tables_data.sh`
