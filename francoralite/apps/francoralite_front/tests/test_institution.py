from django.utils.translation import gettext as _

def test_institution_list(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the locations list page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/institution')

         # Verify the label of the institution page
        francoralite_context.verify_title(_('Institutions'))

        # links to the institutions
        link_view_1 = francoralite_context.find_element(by_link_url='/institution/1')
        assert link_view_1.text == 'Université de Poitiers'

        # Verify buttons
        has_buttons = username in francoralite_context.ADMINS
        assert has_buttons == francoralite_context.exists_element(by_link_url='/institution/edit/1')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/institution/delete/1')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)

def test_institution_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the first fond page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/institution/1')

        # Verify the label of the institution page
        francoralite_context.verify_title("Institution : Université de Poitiers")

        # Verify data
        data = {
            'id_notes': '',
        }
        francoralite_context.verify_data(data)

        # Verify buttons
        has_buttons = username in francoralite_context.ADMINS
        assert has_buttons == francoralite_context.exists_element(by_link_url='/institution/edit/1')

        has_buttons = username in francoralite_context.WRITERS
        assert has_buttons == francoralite_context.exists_element(by_link_url='/institution/1/fond/add')
        assert has_buttons == francoralite_context.exists_element(by_link_url='/fond/edit/1')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/fond/delete/1')
        assert has_buttons == francoralite_context.exists_element(by_link_url='/fond/edit/2')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/fond/delete/2')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)

def test_institution_add(francoralite_context):
    # Go to the home page
    francoralite_context.open_homepage(auth_username='administrateur')

    francoralite_context.move_to_element(by_css_selector='img')
    # Move pointer to open the sub-menu
    francoralite_context.move_to_element(by_link_text=_('Archives sonores'))

    # Click on the institution menu
    francoralite_context.find_element(by_link_text=_('Institutions')).click()

    # Verify the label "Institutions"
    francoralite_context.verify_title(_('Institutions'))

    # Click on the "add" link
    francoralite_context.find_element(by_link_class='btn_add').click()

    # Verify the label "Institutions - Création"
    francoralite_context.verify_title(_('Institutions - Création'))

    # Write content
    francoralite_context.find_element(by_id='id_name').send_keys('Institution Test')
    francoralite_context.find_element(by_div_class='ProseMirror').send_keys('Ceci est une institution de **test**.')

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Goto to list of institution
    # Verify the label "Institutions"
    francoralite_context.verify_title(_('Institutions'))

    # Click on the new institution created
    francoralite_context.find_element(by_link_text='Institution Test').click()

    # Check values
    # Verify the label "Institution : Institution Test"
    francoralite_context.verify_title('Institution : Institution Test')
