from django.utils.translation import gettext as _


def test_collection_list(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the collections list page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/collection')

        # Verify the label of the collection page
        francoralite_context.verify_title(_('Enquêtes'))

        # links to the collections
        link_view_1 = francoralite_context.find_element(by_link_url='/collection/1')
        assert link_view_1.text == 'UPOI_AFE_0000_0001'

        link_view_2 = francoralite_context.find_element(by_link_url='/collection/2')
        assert link_view_2.text == 'UPOI_ATP_0001_0001'

        has_buttons = username in ('contributeur', 'administrateur')
        assert has_buttons == francoralite_context.exists_element(by_link_url='/collection/edit/1')
        assert has_buttons == francoralite_context.exists_element(by_link_url='/collection/edit/2')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/collection/delete/1')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/collection/delete/2')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_collection_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the first collection page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/collection/1')

        # Verify data
        data = {
            'id_title': "Répertoire chanté de Sœur Cécilia McGraw au Nouveau-Brunswick [Extrait d'enquête]",
            'id_description': "Extrait d'enquête de Sœur Jeanne d'Arc Lortie le 15 mars 1963 auprès de Sœur Cécilia McGraw (53 ans).",
            'id_code': 'UPOI_AFE_0000_0001',
            'id_recorded_from_year': '1963-01-01',
            'id_recorded_to_year': '1963-01-02',
            'id_year_published': '',
            'id_legal_rights': 'domaine public',
        }
        francoralite_context.verify_data(data)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_collection_add(francoralite_context):
    # Go to the first collection page
    francoralite_context.open_homepage(auth_username='contributeur')
    francoralite_context.open_url('/mission/1')

    # Verify the label of the collection page
    francoralite_context.verify_title("Mission : Extraits d'enquêtes du fonds Archives de Folklore et d'Ethnologie [Exemple]")

    # Click on the "add" link
    francoralite_context.find_element(by_link_url='/institution/1/fond/1/mission/1/collection/add').click()

    # Write content
    content = {
        'id_title': 'Collection test',
        'id_recorded_from_year': '1995-01-01',
        'id_recorded_to_year': '2015-01-02',
        'id_year_published': 2021,
        'id_legal_rights': 'domaine public',
    }
    francoralite_context.fill_data(content)

    # Write special content
    code = 'upoi_afe_0000_0002'
    francoralite_context.set_element_value('id_code', code)
    content['id_code'] = code.upper()

    description = 'Ceci est une collection de test.'
    francoralite_context.find_element(by_div_class='ProseMirror').send_keys(description)
    content['id_description'] = description

    year_published = '2021'
    francoralite_context.set_element_value('id_year_published', year_published)
    content['id_year_published'] = year_published

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Go to the new collection
    francoralite_context.open_url('/collection/3')

    # Verify content
    francoralite_context.verify_data(content)

def test_collection_update(francoralite_context):
    for username in francoralite_context.WRITERS:
        # Go to the home page
        francoralite_context.open_homepage(auth_username=username)

        # Go to the first collection edit page
        francoralite_context.open_url('/collection/edit/1')

        test_alt_tile = "Test titre original"
        # Write an alt title
        francoralite_context.set_element_value('id_alt_title', test_alt_tile)

        # Validation
        francoralite_context.find_element(by_id='save').click()

        # The collection alt title updated on the detail page
        francoralite_context.open_url('/collection/1')
        label = francoralite_context.find_element(by_id="id_alt_title")
        assert label.text == test_alt_tile

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
            

def test_collection_409_err(francoralite_context):
    for username in francoralite_context.WRITERS:
        # Go to the home page
        francoralite_context.open_homepage(auth_username=username)

        # Go to the first collection edit page
        francoralite_context.open_url('/collection/edit/2')

        # Write a code
        francoralite_context.set_element_value('id_code', 'UPOI_AFE_0000_0001')

        # Validation
        francoralite_context.find_element(by_id='save').click()

        # Message for error HTTP 409
        message = francoralite_context.find_element(by_id="id_message")
        assert message.text == _('Une fiche avec ce code existe déjà.')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
