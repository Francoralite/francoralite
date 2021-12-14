from django.utils.translation import gettext as _


def test_dance_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the first dance page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/dance/1')

        # Verify data
        data = {
            'id_name' : 'polka',
            'id_notes' : 'Notes de polka',
        }
        francoralite_context.verify_title('Genre de danse : polka')
        francoralite_context.verify_data(data)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)


def test_dance_add(francoralite_context):
    # Go to the dance add page
    francoralite_context.open_homepage(auth_username='administrateur')
    francoralite_context.open_url('/dance/add')

    # On page add
    francoralite_context.verify_title(_('Genre de danse - Création'))

    # Write content
    content = {
        'id_name': 'bourree',
        'id_notes': 'Bourrée',
    }
    francoralite_context.fill_data(content)

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Go to the new dance
    francoralite_context.open_url('/dance/4')

    # Verify data
    francoralite_context.verify_title('Genre de danse : bourree')
    francoralite_context.verify_data(content)
