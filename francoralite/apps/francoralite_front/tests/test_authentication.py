from django.utils.translation import gettext as _
from selenium.common.exceptions import NoSuchElementException


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


def test_login_next_page(francoralite_context):
    # Go to the items page list
    francoralite_context.open_url('/item')

    # Check not already logged in
    try:
        francoralite_context.find_element(by_link_class='logout')
    except NoSuchElementException:
        pass  # authentication is required
    else:
        raise RuntimeError('Logout button found: user already logged in')

    # Verify the label of the page
    francoralite_context.verify_title(_('Items'))

    # User login action
    francoralite_context.login(auth_username='contributeur')

    # Verify the label of the page
    francoralite_context.verify_title(_('Items'))

    # Verify the logout button
    francoralite_context.find_element(by_link_class='logout')


def test_logout(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the homepage for each profile
        francoralite_context.open_homepage(auth_username=username)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
