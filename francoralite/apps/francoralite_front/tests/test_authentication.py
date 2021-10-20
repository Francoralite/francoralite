from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from django.utils.translation import gettext as _

def test_login(francoralite_selenium_context):
    # Go to the home page
    browser = francoralite_selenium_context.homepage()

    # Click on the authentication menu
    link_page = browser.find_element(By.XPATH, '//a[text()="' + _("Se connecter") + '"]')
    link_page.click()
    
    # Land on Keycloak authentication page
    title_page = browser.find_element(By.ID, "kc-header-wrapper")
    assert title_page.text == "FRANCORALITE"

    # Write login and password
    username = browser.find_element(By.ID, 'username')
    username.send_keys('contributeur')

    password = browser.find_element(By.ID, 'password')
    password.send_keys('password')

    # Click on submit button (submit action doesn't work)
    button = browser.find_element(By.ID, 'kc-login')
    button.click()

    # Home page with authentication
    # -----------------------------
    # Test username link text
    link_user = browser.find_element(By.XPATH, "//a[contains(@class, 'login')]")
    assert link_user.text == "contributeur"

    # Test logout link text
    link_logout = browser.find_element(By.XPATH, "//a[contains(@class, 'logout')]")
    assert link_logout.text == _("Déconnexion")

    #browser.save_screenshot('./login.png')