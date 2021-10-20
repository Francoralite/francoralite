from django.core.management import call_command
from selenium import webdriver
import pytest


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

    def homepage(self):
        return self.get_url('/')
