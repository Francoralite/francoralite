from selenium.webdriver.common.by import By
from django.utils.translation import gettext as _

def test_institution_add(francoralite_selenium_context):
    # Go to the home page
    browser = francoralite_selenium_context.homepage(auth=True, username='administrateur')

    # Click on the institution menu
    link_page = browser.find_element(By.XPATH, '//a[text()="' + _("Institutions") + '"]')
    link_page.click()

    # Verify the label "Institutions"
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Institutions")

    # Click on the "add" link
    link_add = browser.find_element(By.XPATH, "//a[contains(@class, 'btn_add')]")
    link_add.click()

    # Verify the label "Institutions - Création"
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Institutions - Création")

    # Write content
    id_name = browser.find_element(By.ID, 'id_name')
    id_name.send_keys(_('Institution Test'))

    editor = browser.find_element(By.XPATH, "//div[contains(@class, 'ProseMirror')]")
    editor.send_keys('Ceci est une institution de **test**.')

    # Validation
    button_valid = browser.find_element(By.XPATH, "//*[@id='save']")
    button_valid.click()

    # Goto to list of institution
    # Verify the label "Institutions"
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Institutions")
    
    # Click on the new institution created
    new_institution = browser.find_element(By.XPATH, '//a[text()="' + _("Institution Test") + '"]')
    new_institution.click()

    # Check values
    # Verify the label "Institution : Institution Test"
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Institution : Institution Test")
