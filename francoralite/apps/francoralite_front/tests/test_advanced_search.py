from django.utils.translation import gettext as _


URL_PREFIX = '/search_advanced/'


def test_search(francoralite_context):
    criteria = [
        {
            'id_block': 'details_genders',
            'id_field': 'thematic',
            'value': 'r',
            'option': "récit",
            'id_checkbox' : 'domains_deposit'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'domain_song',
            'value': 'm',
            'option': "mariage",
            'id_checkbox' : 'domains_song'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'timbre_ref',
            'value': 'ti',
            'option': "timbre_ref_1",
            'id_checkbox' : 'domains_song'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'timbre',
            'value': 'ti',
            'option': "timbre_1",
            'id_checkbox' : 'domains_song'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'coupe',
            'value': 'a',
            'option': "AABB",
            'id_checkbox' : 'domains_song'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'coirault',
            'value': '9',
            'option': "9003 : À l’arrivée du doux printemps",
            'id_checkbox' : 'domains_song'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'domain_vocal',
            'value': 'c',
            'option': "comptine",
            'id_checkbox' : 'domains_vocal'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'coirault',
            'value': '9',
            'option': "9003 : À l’arrivée du doux printemps",
            'id_checkbox' : 'domains_vocal'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'domain_music',
            'value': 'ai',
            'option': "air de chanson",
            'id_checkbox' : 'domains_music'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'instrument',
            'value': 'v',
            'option': "Violon",
            'id_checkbox' : 'domains_music'
        },
        {
            'id_block': 'details_genders',
            'id_field': 'domain_tale',
            'value': 'c',
            'option': "conte facétieux",
            'id_checkbox' : 'domains_tale'
        },
        {
            'id_block': 'details_references',
            'id_field': 'code_internal',
            'value': 'upoi',
            'option': 'UPOI_AFE',
        },
        {
            'id_block': 'details_references',
            'id_field': 'code_external',
            'value': '56',
            'option': '56-10-199 OU 56-10-138 -714-15',
        },
        {
            'id_block': 'details_what',
            'id_field': 'dance',
            'value': 'va',
            'option': 'valse',
        },
        {
            'id_block': 'details_what',
            'id_field': 'keyword',
            'value': 'grap',
            'option': 'biographie',
        },
        {
            'id_block': 'details_what',
            'id_field': 'language',
            'value': 'fr',
            'option': 'Créoles et pidgins basés sur le français',
        },
        {
            'id_block': 'details_what',
            'id_field': 'media_type',
            'value': 'au',
            'option': 'cassette audio',
        },
        {
            'id_block': 'details_what',
            'id_field': 'recording_context',
            'value': 'en',
            'option': 'enquête',
        },
        {
            'id_block': 'details_what',
            'id_field': 'usefulness',
            'value': 'da',
            'option': 'danser',
        },
        {
            'id_block': 'details_where',
            'id_field': 'location',
            'value': 'poi',
            'option': "Poitiers, Vienne, Nouvelle-Aquitaine, France métropolitaine, 86000, France",
        },
        {
            'id_block': 'details_where',
            'id_field': 'cultural_area',
            'value': 'poi',
            'option': "Saintonge, Poitou",
        },
        {
            'id_block': 'details_who',
            'id_field': 'informer_civility',
            'value': 'mo',
            'option': 'Monsieur',
        },
        {
            'id_block': 'details_who',
            'id_field': 'informer',
            'value': 'aub',
            'option': 'Charles Aubrière',
        },
        {
            'id_block': 'details_who',
            'id_field': 'collector_civility',
            'value': 'ml',
            'option': 'Mlle',
        },
        {
            'id_block': 'details_who',
            'id_field': 'collector',
            'value': 'cl',
            'option': 'Claudie Marcel-Dubois',
        },
    ]

    for crit in criteria:
        from icecream import ic
        ic.configureOutput(includeContext=True)
        ic(crit)

        # Go to advanced search page
        francoralite_context.open_url(URL_PREFIX)

        # Verify the label of the page
        francoralite_context.verify_title(_('Recherche avancée'))

        # Open the block
        francoralite_context.scroll_to_element(by_id=crit['id_block']).click()

        # Click on checkbox if required
        if 'id_checkbox' in crit:
            francoralite_context.scroll_to_element(by_id=crit['id_checkbox']).click()

        # Write first characters of the content
        francoralite_context.scroll_to_element(by_id=crit['id_field']).send_keys(crit['value'])

        # There is an option named "{option}"
        component = '*[starts-with(local-name(), "francoralite-")][@name="' + crit['id_field'] + '"]'
        francoralite_context.find_element(
            by_xpath=f"//{component}/ul/li[contains(text(), '{crit['option']}')]",
            visibility_timeout=5,
        )


def test_links_to_list(francoralite_context):

    links = [
        {
            'id_block': 'details_genders',
            'id_checkbox': 'domains_song',
            'id_link': 'link_coupe',
            'title': 'Coupe',
        },
        {
            'id_block': 'details_genders',
            'id_checkbox': 'domains_music',
            'id_link': 'link_domain_music',
            'title': 'Genre de musique',
        },
        {
            'id_block': 'details_genders',
            'id_checkbox': 'domains_song',
            'id_link': 'link_domain_song',
            'title': 'Genre de chanson',
        },
        {
            'id_block': 'details_genders',
            'id_checkbox': 'domains_tale',
            'id_link': 'link_domain_tale',
            'title': 'Genre de conte',
        },
        {
            'id_block': 'details_genders',
            'id_checkbox': 'domains_vocal',
            'id_link': 'link_domain_vocal',
            'title': 'Genre vocal',
        },
        {
            'id_block': 'details_genders',
            'id_checkbox': 'domains_music',
            'id_link': 'link_instrument',
            'title': 'Voix/Instruments',
        },
        {
            'id_block': 'details_genders',
            'id_checkbox': 'domains_deposit',
            'id_link': 'link_thematic',
            'title': 'Thématique',
        },
        {
            'id_block': 'details_what',
            'id_link': 'link_dance',
            'title': 'Genre de danse',
        },
        {
            'id_block': 'details_what',
            'id_link': 'link_keyword',
            'title': 'Mot-clé',
        },
        {
            'id_block': 'details_what',
            'id_link': 'link_language',
            'title': 'Langue',
        },
        {
            'id_block': 'details_what',
            'id_link': 'link_media_type',
            'title': 'Type de média',
        },
        {
            'id_block': 'details_what',
            'id_link': 'link_recording_context',
            'title': 'Contexte d’enregistrement',
        },
        {
            'id_block': 'details_what',
            'id_link': 'link_usefulness',
            'title': 'Fonction',
        },
        {
            'id_block': 'details_where',
            'id_link': 'link_location',
            'title': 'Lieux',
        },
        {
            'id_block': 'details_who',
            'id_link': 'link_authority_collector',
            'title': 'Enquêteurs',
        },
        {
            'id_block': 'details_who',
            'id_link': 'link_authority_informer',
            'title': 'Informateurs',
        },
    ]

    for link in links:
        from icecream import ic
        ic.configureOutput(includeContext=True)
        ic(link)

        # Go to advanced search page
        francoralite_context.open_url(URL_PREFIX)

        # Scroll to block
        francoralite_context.scroll_to_element(by_id=link['id_block']).click()

        # Click on checkbox if required
        if 'id_checkbox' in link:
            francoralite_context.scroll_to_element(by_id=link['id_checkbox']).click()

        # Click on link to open list in a new tab
        element = francoralite_context.scroll_to_element(by_id=link['id_link'])
        new_tab = francoralite_context.click_and_switch_to_new_tab(element)

        # Verify the title and close the new tab
        francoralite_context.verify_title(link['title'], visibility_timeout=5)
        francoralite_context.close_tab(new_tab)
