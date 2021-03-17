tables=("acquisition_modes" \
  "ad_conversions" \
  "context_keywords" \
  "copy_type" \
  "ethnic_group_aliases" \
  "ethnic_groups" \
  "generic_styles" \
  "identifier_type" \
  "instrument_alias_relations" \
  "instrument_aliases" \
  "instrument_relations" \
  "instruments" \
  "languages" \
  "legal_rights" \
  "location_aliases" \
  "location_relations" \
  "location_types" \
  "locations" \
  "media_analysis" \
  "media_collection_identifier" \
  "media_collection_related" \
  "media_collections" \
  "media_corpus" \
  "media_corpus_related" \
  "media_fonds" \
  "media_fonds_related" \
  "media_formats" \
  "media_item_identifier" \
  "media_item_keywords" \
  "media_item_performances" \
  "media_item_related" \
  "media_items" \
  "media_markers" \
  "media_parts" \
  "media_status" \
  "media_transcoding" \
  "media_type" \
  "metadata_authors" \
  "metadata_writers" \
  "organization" \
  "original_channel_number" \
  "original_format" \
  "physical_formats" \
  "playlist_resources" \
  "playlists" \
  "profiles" \
  "publisher_collections" \
  "publishers" \
  "publishing_status" \
  "recording_contexts" \
  "revisions" \
  "rights" \
  "search_criteria" \
  "searches" \
  "tape_length" \
  "tape_speed" \
  "tape_vendor" \
  "tape_wheel_diameter" \
  "tape_width" \
  "telemeta_enumerationproperty" \
  "telemeta_media_transcoded" \
  "topic" \
  "vernacular_styles")

for table in "${tables[@]}"
do
    count=$(mysql -s -N -u "${MYSQL_USER}" -p"${MYSQL_PASSWORD}" "${MYSQL_DATABASE}" -e "SELECT COUNT(*) FROM ${table};" 2>/dev/null)
    echo "${table} : ${count}"

    #if [ $count -ne 0 ]
    #then
    #    mysql -u "${MYSQL_USER}" -p"${MYSQL_PASSWORD}" "${MYSQL_DATABASE}" -e "SELECT * FROM ${table};" 2>/dev/null
    #fi
done
