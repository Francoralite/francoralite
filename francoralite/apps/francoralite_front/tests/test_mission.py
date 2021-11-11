from django.utils.translation import gettext as _


def test_mission_list(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the missions list page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/mission')

        # Verify the label of the mission page
        francoralite_context.verify_title(_('Missions'))

        # links to the missions
        link_view_1 = francoralite_context.find_element(by_link_url='/mission/1')
        assert link_view_1.text == 'UPOI_AFE_0000'

        link_view_2 = francoralite_context.find_element(by_link_url='/mission/2')
        assert link_view_2.text == 'UPOI_ATP_0000'

        has_buttons = username in ('contributeur', 'administrateur')
        assert has_buttons == francoralite_context.exists_element(by_link_url='/mission/edit/1')
        assert has_buttons == francoralite_context.exists_element(by_link_url='/mission/edit/2')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/mission/delete/1')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/mission/delete/2')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_mission_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the first mission page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/mission/1')

        # Verify data
        data = {
            'id_title': "Extraits d'enquêtes du fonds Archives de Folklore et d'Ethnologie [Exemple]",
            'id_description': "Sélection de copies commandées par Joseph Le Floc'h en 1994 aux Archives de Folklore de l'Université Laval, pour ses cours sur la chanson de tradition orale franco-canadienne au Département de Musicologie de l'Université de Poitiers.\nLes Archives de folklore et d'ethnologie sont constituées des fonds et des collections, privés ou publics, concernant la culture des francophones en Amérique du Nord. Cette documentation reflète les manifestations tant esthétiques que pragmatiques de cette culture, soit les us et coutumes, les légendes, les contes, les chansons, les métiers, le costume, la religion, la musique, les histoires de vie, etc. Elle se base principalement sur des enquêtes sur le terrain mais aussi sur des dépouillements bibliographiques et des travaux de recherche.",
            'id_code': 'UPOI_AFE_0000',
        }

        francoralite_context.verify_data(data)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_mission_add(francoralite_context):
    # Go to the fonds page
    francoralite_context.open_homepage(auth_username='contributeur')
    francoralite_context.open_url('/fond/1')

    # Verify the label of the fonds page
    francoralite_context.verify_title(_("Fonds : Fonds issus des Archives de Folklore et d'Ethnologie [Exemple]"))

    # Click on the "add" link
    francoralite_context.find_element(by_link_url='/institution/1/fond/1/mission/add').click()

    # Write content
    content = {
        'id_code_partner': 'TEST 000',
        'id_title': 'Mission de test',
        'id_public_access': 'full',
    }
    francoralite_context.fill_data(content)
    del content['id_public_access']

    # Write special content
    code = 'upoi_afe_0001'
    francoralite_context.set_element_value('id_code', code)
    content['id_code'] = code.upper()

    description = 'Ceci est une mission de test.'
    francoralite_context.find_element(by_div_class='ProseMirror').send_keys(description)
    content['id_description'] = description

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Go to the new mission
    francoralite_context.open_url('/mission/4')

    # Verify content
    francoralite_context.verify_data(content)
