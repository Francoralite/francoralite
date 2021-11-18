from django.utils.translation import gettext as _


def test_login(francoralite_context):
    # Go to the home page, with authentication
    francoralite_context.open_homepage(auth_username='contributeur')

    # Test username link text
    link_user = francoralite_context.find_element(by_link_class='login')
    assert link_user.text == 'contributeur'

    # Test logout link text
    link_logout = francoralite_context.find_element(by_link_class='logout')
    assert link_logout.text == _('Déconnexion')

    #francoralite_context.save_screenshot('./login.png')


def test_logout(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the homepage for each profile
        francoralite_context.open_homepage(auth_username=username)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
