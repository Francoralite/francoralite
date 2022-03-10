from django.utils.translation import gettext as _


def test_authority_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the authorities list page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/authority/1')

        # Verify data
        data = {
            'id_last_name': 'Le Gaulois',
            'id_first_name': 'Astérix',
            'id_civility': '',
            'id_alias': '',
            'id_birth_date': '',
            'id_birth_location': '',
            'id_death_date': '',
            'id_death_location': '',
            'id_biography': '',
            'id_uri': '',
        }
        francoralite_context.verify_title('Personne : Le Gaulois Astérix')
        francoralite_context.verify_data(data)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_authority_add(francoralite_context):
    # Go to the home page
    francoralite_context.open_homepage(auth_username='contributeur')

    # Click on authority menu
    francoralite_context.find_element(by_link_text=_('Personnes')).click()

    # On authority list
    francoralite_context.verify_title(_('Personnes'))

    # Click on the "add" link
    francoralite_context.find_element(by_link_url='/authority/add').click()

    # Write content
    content = {
        'id_last_name' : 'verne',
        'id_first_name' : 'jules',
        'id_alias' : 'julot',
        'id_civility' : 'mr',
        'id_birth_date' : '1828-02-08',
        'id_death_date' : '1905-03-24',
        'id_uri' : 'https://fr.wikipedia.org/wiki/Jules_Verne',
    }
    francoralite_context.fill_data(content)

    biography = 'Jules Verne, né le 8 février 1828 à Nantes et mort le 24 mars 1905 à Amiens, est un écrivain français'
    francoralite_context.find_element(by_div_class='ProseMirror').send_keys(biography)

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Go to the new authority
    francoralite_context.open_url('/authority/10')

    # Verify data
    content['id_biography'] = biography
    content['id_birth_location'] = ''
    content['id_death_location'] = ''

    francoralite_context.verify_title('Personne : verne jules')
    francoralite_context.verify_data(content)


def test_authority_birth_location(francoralite_context):
    _test_location_update(francoralite_context, field_name='id_birth_location')


def test_authority_death_location(francoralite_context):
    _test_location_update(francoralite_context, field_name='id_death_location')


def _test_location_update(francoralite_context, field_name):
    # Go to the home page
    francoralite_context.open_homepage(auth_username='contributeur')

    # Go to the first authority edit page
    francoralite_context.open_url('/authority/edit/1')

    # Write first characters of the content
    francoralite_context.find_element(by_id=field_name + '_name').send_keys('poi')

    # Select first proposal
    francoralite_context.move_to_element(
        by_css_selector='#%s_name ~ div .tt-dataset' % field_name,
        visibility_timeout=1,
    ).click()

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # The location is visible on the detail page
    francoralite_context.open_url('/authority/1')
    label = francoralite_context.find_element(by_id=field_name)
    assert label.text == 'Poitiers, Vienne, Nouvelle-Aquitaine, France métropolitaine, 86000, France'

    # Return to the edit page
    francoralite_context.open_url('/authority/edit/1')

    # Clear the field content
    francoralite_context.clear_element(by_id=field_name + '_name')

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Verify that the location is empty on the detail page
    francoralite_context.open_url('/authority/1')
    label = francoralite_context.find_element(by_id=field_name)
    assert label.text == ''
