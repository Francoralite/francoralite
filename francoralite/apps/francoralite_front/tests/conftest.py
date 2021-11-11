from django.core.management import call_command
from django.utils.translation import gettext as _
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture(scope='function')
def francoralite_context(live_server, settings, django_db_blocker):

    settings.FRONT_HOST_URL = live_server.url
    settings.FRONT_HOST_URL_EXTERNAL = live_server.url
    settings.LOGIN_REDIRECT_URL = live_server.url

    with django_db_blocker.unblock():
        call_command('loaddata', 'francoralite.json')

    context = FrancoraliteSeleniumContext(live_server.url)
    yield context

    context.browser.quit()


class FrancoraliteSeleniumContext():

    USERNAMES = (
        '',  # anonymous
        'utilisateur',
        'contributeur',
        'administrateur',
    )

    def __init__(self, url_prefix=None):
        self.URL_PREFIX = url_prefix or 'http://127.0.0.1:8000'
        options = FirefoxOptions()
        options.headless = True
        options.firefox_path = '/usr/bin/firefox-esr'
        self.browser = Firefox(options=options)

    def open_url(self, url):
        self.browser.get(self.URL_PREFIX + url)

    def open_homepage(self, auth_username=None):
        self.open_url('/')

        if auth_username:
            # Test logout link text
            try:
                link_logout = self.find_element(by_link_class='logout')
            except NoSuchElementException:
                pass  # authentication is required
            else:
                if link_logout.text == _('Déconnexion'):
                    return

            # Authentication
            # ---------------

            # Click on the authentication menu
            self.find_element(by_link_text=_('Se connecter')).click()

            # Land on Keycloak authentication page
            title_page = self.find_element(by_id='kc-header-wrapper')
            assert title_page.text == 'FRANCORALITE'

            # Write login and password
            self.find_element(by_id='username').send_keys(auth_username)
            self.find_element(by_id='password').send_keys('password')

            # Click on submit button (submit action doesn't work)
            self.find_element(by_id='kc-login').click()

    def logout(self, current_username):

        # Test username link text
        link_user = self.find_element(by_link_class='login')
        assert link_user.text == current_username

        # Test logout link text
        link_logout = self.find_element(by_link_class='logout')
        assert link_logout.text == _('Déconnexion')

        # Click on logout link
        link_logout.click()

        # Test the login link exists
        link_page = self.find_element(by_link_text=_('Se connecter'))
        assert link_page.text == _('Se connecter')

    def find_elements(self, parent=None, **kwargs):

        # Prepare "by" critera for find request
        criteria = self._get_find_elements_criteria(**kwargs)

        # Use root node as parent search if empty
        if parent is None:
            parent = self.browser

        # Find elements
        return parent.find_elements(*criteria)

    def find_element(self, parent=None, visibility_timeout=None, **kwargs):

        # Prepare "by" critera for find request
        criteria = self._get_find_elements_criteria(**kwargs)

        # Use root node as parent search if empty
        if parent is None:
            parent = self.browser

        # Find element
        if visibility_timeout is not None:
            return WebDriverWait(parent, visibility_timeout).until(
                EC.visibility_of_element_located(criteria))
        else:
            return parent.find_element(*criteria)

    def _get_find_elements_criteria(self,
        by_id=None, by_xpath=None, by_css_selector=None,
        by_class_name=None, by_link_text=None, by_link_url=None,
        by_link_class=None, by_button_url=None, by_div_class=None):

        # Verify unique "by" parameter filled
        if len([param for param in (
            by_id,
            by_xpath,
            by_css_selector,
            by_class_name,
            by_link_text,
            by_link_url,
            by_link_class,
            by_button_url,
            by_div_class,
        ) if param is not None]) > 1:
            raise TypeError('too many "by" parameters')

        # Prepare "by" critera for find request
        if by_id is not None:
            return (By.ID, by_id)
        elif by_xpath is not None:
            return (By.XPATH, by_xpath)
        elif by_css_selector is not None:
            return (By.CSS_SELECTOR, by_css_selector)
        elif by_class_name is not None:
            return (By.CLASS_NAME, by_class_name)
        elif by_link_text is not None:
            return (By.XPATH, '//a[text()="%s"]' %
                    by_link_text.replace('\\', '\\\\').replace('"', '\\"'))
        elif by_link_url is not None:
            return (By.XPATH, '//a[@href="%s"]' %
                    by_link_url.replace('\\', '\\\\').replace('"', '\\"'))
        elif by_link_class is not None:
            return (By.XPATH, '//a[contains(@class, "%s")]' %
                    by_link_class.replace('\\', '\\\\').replace('"', '\\"'))
        elif by_button_url is not None:
            return (By.XPATH, '//button[@data-url="%s"]' %
                    by_button_url.replace('\\', '\\\\').replace('"', '\\"'))
        elif by_div_class is not None:
            return (By.XPATH, '//div[contains(@class, "%s")]' %
                    by_div_class.replace('\\', '\\\\').replace('"', '\\"'))
        else:
            raise TypeError('no "by" parameter found')

    def exists_element(self, **kwargs):
        try:
            self.find_element(**kwargs)
        except (NoSuchElementException, TimeoutException):
            return False
        else:
            return True

    def move_to_element(self, **kwargs):
        element = self.find_element(**kwargs)
        ActionChains(self.browser).move_to_element(element).perform()
        return element

    def clear_element(self, **kwargs):
        element = self.find_element(**kwargs)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)
        return element

    def set_element_value(self, by_id, value):
        self.browser.execute_script(
            'document.getElementById("%s").value="%s"' % (
                by_id.replace('\\', '\\\\').replace('"', '\\"'),
                value.replace('\\', '\\\\').replace('"', '\\"'),
            )
        )

    def fill_data(self, data):
        for element_id, element_value in data.items():
            self.find_element(by_id=element_id).send_keys(element_value)

    def verify_data(self, data):
        for element_id, element_value in data.items():
            element = self.find_element(by_id=element_id)
            assert element.text == element_value

    def verify_title(self, value):
        assert self.find_element(by_xpath='//main/h1').text == value

    def save_screenshot(self, *args, **kwargs):
        return self.browser.save_screenshot(*args, **kwargs)
