from selenium.webdriver.common.by import By
from django.utils.translation import gettext as _

def test_login(francoralite_selenium_context):
    # Go to the home page, with authentication
    browser = francoralite_selenium_context.homepage(auth=True)

    # Test username link text
    link_user = browser.find_element(By.XPATH, "//a[contains(@class, 'login')]")
    assert link_user.text == "contributeur"

    # Test logout link text
    link_logout = browser.find_element(By.XPATH, "//a[contains(@class, 'logout')]")
    assert link_logout.text == _("Déconnexion")

    #browser.save_screenshot('./login.png')

def test_logout(francoralite_selenium_context):
    # Go to the home page, with authentication
    browser = francoralite_selenium_context.homepage(auth=True)

    # Test username link text
    link_user = browser.find_element(By.XPATH, "//a[contains(@class, 'login')]")
    assert link_user.text == "contributeur"

    # Test logout link text
    link_logout = browser.find_element(By.XPATH, "//a[contains(@class, 'logout')]")
    assert link_logout.text == _("Déconnexion")

    link_logout.click()

    link_page = browser.find_element(By.XPATH, '//a[text()="' + _("Se connecter") + '"]')
    assert link_page.text == _("Se connecter")
