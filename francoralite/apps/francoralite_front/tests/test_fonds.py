from django.utils.translation import gettext as _


def test_fonds_list(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the fonds list page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/fond')

        # Verify the label of the fonds page
        francoralite_context.verify_title(_('Fonds'))

        # links to the fonds
        link_view_1 = francoralite_context.find_element(by_link_url='/fond/1')
        assert link_view_1.text == 'UPOI_AFE'

        link_view_2 = francoralite_context.find_element(by_link_url='/fond/2')
        assert link_view_2.text == 'UPOI_ATP'

        has_buttons = username in ('contributeur', 'administrateur')
        assert has_buttons == francoralite_context.exists_element(
            by_link_url='/fond/edit/1')
        assert has_buttons == francoralite_context.exists_element(
            by_link_url='/fond/edit/2')
        assert has_buttons == francoralite_context.exists_element(
            by_button_url='/fond/delete/1')
        assert has_buttons == francoralite_context.exists_element(
            by_button_url='/fond/delete/2')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_fonds_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the first fond page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/fond/1')

        # Verify data
        data = {
            'id_code': 'UPOI_AFE',
            'id_description': "Les Archives de Folklore et d'Ethnologie sont constituées des fonds et des collections, privés ou publics, concernant la culture des francophones en Amérique du Nord. Cette documentation reflète les manifestations tant esthétiques que pragmatiques de cette culture, soit les us et coutumes, les légendes, les contes, les chansons, les métiers, le costume, la religion, la musique, les histoires de vie, etc. Elle se base principalement sur des enquêtes sur le terrain mais aussi sur des dépouillements bibliographiques et des travaux de recherche.",
            'id_conservation_site': 'Poitiers',
        }
        francoralite_context.verify_data(data)

        # Verify duration
        francoralite_context.open_url('/fond/2')
        data = {
            'id_code': 'UPOI_ATP',
            'id_duration' : '0:03:50',
        }
        francoralite_context.verify_data(data)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_fonds_add(francoralite_context):
    # Go to the home page
    francoralite_context.open_homepage(auth_username='contributeur')

    francoralite_context.move_to_element(by_css_selector='img')
    # Move pointer to open the sub-menu
    francoralite_context.move_to_element(by_link_text=_('Archives sonores'))
    # Click on the institution menu
    francoralite_context.scroll_to_element(by_link_text=_('Institutions')).click()

    # Verify the label "Institutions"
    francoralite_context.verify_title(_('Institutions'))

    # Click on the fonds link
    francoralite_context.find_element(
        by_link_text='Université de Poitiers').click()

    # Verify the label of the fonds page
    francoralite_context.verify_title(
        _('Institution : Université de Poitiers'))

    # Click on the "add" link
    francoralite_context.find_element(by_link_text=_('Créer un fonds')).click()

    # Write content
    content = {
        'id_code_partner': 'TEST 000',
        'id_title': 'Fonds de test',
        'id_conservation_site': 'Lieu test',
    }
    francoralite_context.fill_data(content)

    # Write special content
    code = 'upoi_tst'
    francoralite_context.set_element_value('id_code', code)
    content['id_code'] = code.upper()

    description = 'Ceci est un fonds de test.'
    francoralite_context.find_element(
        by_div_class='ProseMirror').send_keys(description)
    content['id_description'] = description

    comment = 'Un beau commentaire.'
    francoralite_context.set_element_value('id_comment', comment)
    content['id_comment'] = comment

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Go to the new fonds
    francoralite_context.open_url('/fond/3')

    # Verify content
    del content['id_title']
    francoralite_context.verify_data(content)


def test_fonds_update(francoralite_context):
    for username in francoralite_context.WRITERS:
        # Go to the home page
        francoralite_context.open_homepage(auth_username=username)

        # Go to the first fonds edit page
        francoralite_context.open_url('/fond/edit/1')

        # Write a code partner
        francoralite_context.set_element_value('id_code_partner', 'TEST_CODE')

        # Validation
        francoralite_context.find_element(by_id='save').click()

        # The mission code partner updated on the detail page
        francoralite_context.open_url('/fond/1')
        label = francoralite_context.find_element(by_id="id_code_partner")
        assert label.text == 'TEST_CODE'

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_fonds_409_err(francoralite_context):
    for username in francoralite_context.WRITERS:
        # Go to the home page
        francoralite_context.open_homepage(auth_username=username)

        # Go to the first fonds edit page
        francoralite_context.open_url('/fond/edit/1')

        # Write a code
        francoralite_context.set_element_value('id_code', 'UPOI_ATP')

        # Validation
        francoralite_context.find_element(by_id='save').click()

        # Message for error HTTP 409
        message = francoralite_context.find_element(by_id="id_message")
        assert message.text == _('Une fiche avec ce code existe déjà.')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
