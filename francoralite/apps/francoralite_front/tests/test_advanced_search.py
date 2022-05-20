from django.utils.translation import gettext as _


URL_PREFIX = "/search_advanced/"

def select_search_criteria(id_block, id_field, value, option, context):
    # Go to advanced search page
    context.open_url(URL_PREFIX)

    # Verify the label of the page
    context.verify_title(_('Recherche avancée'))

    # Select the block "details_what"
    context.scroll_to_element(by_id=id_block).click()

    # Write first characters of the content
    context.scroll_to_element(by_id=id_field).send_keys(value)

    # There is an option named "{option}"
    context.find_element(
        by_xpath=f"//francoralite-{id_field}/ul/li[contains(text(), '{option}')]",
        visibility_timeout=5,
    )

def test_search(francoralite_context):
    criteria = [
        {
            'id_block':"details_what",
            'id_field':"dance",
            'value':"va",
            'option':"valse",
        },
    ]

    #TODO ajouter des tests pour tous les critères

    for crit in criteria:
        select_search_criteria(
            id_block=crit['id_block'],
            id_field=crit['id_field'],
            value=crit['value'],
            option=crit['option'],
            context=francoralite_context
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
