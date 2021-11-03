from django.core.management import call_command
from django.utils.translation import gettext as _
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope='function')
def all_profiles():
    profiles = {
        'anonymous': [False,''],
        'utilisateur': [True, 'utilisateur'],
        'contributeur': [True, 'contributeur'],
    }
    return profiles.values()

@pytest.fixture(scope='function')
def francoralite_selenium_context(live_server, settings, django_db_blocker):

    settings.FRONT_HOST_URL = live_server.url
    settings.FRONT_HOST_URL_EXTERNAL = live_server.url
    settings.LOGIN_REDIRECT_URL = live_server.url

    with django_db_blocker.unblock():
        call_command('loaddata', 'francoralite.json')

    context = SeleniumContext(live_server.url)
    yield context

    context.browser.quit()


class SeleniumContext():

    def __init__(self, url_prefix=None):
        self.URL_PREFIX = url_prefix or 'http://127.0.0.1:8000'
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.firefox_path = '/usr/bin/firefox-esr'
        self.browser = webdriver.Firefox(options=options)

    def get_url(self, url):
        self.browser.get(self.URL_PREFIX + url)
        return self.browser

    def homepage(self, auth=False, username='contributeur'):
        browser = self.get_url('/')
        
        if auth :
            # Test logout link text
            try:
                link_logout = browser.find_element(By.XPATH, "//a[contains(@class, 'logout')]")
            except NoSuchElementException:
                pass
            else:
                if link_logout.text == _("Déconnexion"):
                    return browser
            
            # Authentication
            # ---------------
            # Click on the authentication menu
            link_page = browser.find_element(By.XPATH, '//a[text()="' + _("Se connecter") + '"]')
            link_page.click()

            # Land on Keycloak authentication page
            title_page = browser.find_element(By.ID, "kc-header-wrapper")
            assert title_page.text == "FRANCORALITE"

            # Write login and password
            field_username = browser.find_element(By.ID, 'username')
            field_username.send_keys(username)

            field_password = browser.find_element(By.ID, 'password')
            field_password.send_keys('password')

            # Click on submit button (submit action doesn't work)
            button = browser.find_element(By.ID, 'kc-login')
            button.click()

        return browser

    def logout(self, browser, username):

        # Test username link text
        link_user = browser.find_element(By.XPATH, "//a[contains(@class, 'login')]")
        assert link_user.text == username

        # Test logout link text
        link_logout = browser.find_element(By.XPATH, "//a[contains(@class, 'logout')]")
        assert link_logout.text == _("Déconnexion")

        link_logout.click()

        link_page = browser.find_element(By.XPATH, '//a[text()="' + _("Se connecter") + '"]')
        assert link_page.text == _("Se connecter")
