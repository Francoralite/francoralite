from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.utils.translation import gettext as _

def verify_data(browser, data):
    # Verify data
 
    label = browser.find_element(By.XPATH,  "//*[@id='id_code']")
    assert label.text == data["code"]

    label = browser.find_element(By.XPATH, "//*[@id='id_title']")
    assert label.text == data["title"]

    label = browser.find_element(By.XPATH, "//*[@id='id_description']")
    assert label.text == data["description"]

def test_fonds_details(francoralite_selenium_context, all_profiles):
    # Open the homepage for each profile 
    for profile in all_profiles:
        francoralite_selenium_context.homepage(auth=profile[0], username=profile[1])
        browser = francoralite_selenium_context.get_url("/fond/1")

        # Verify data
        data = {
            "code" : "UPOI_AFE",
            "title" : "Fonds issus des Archives de Folklore et d'Ethnologie [Exemple]",
            "description" : "Les Archives de Folklore et d'Ethnologie sont constituées des fonds et des collections, privés ou publics, concernant la culture des francophones en Amérique du Nord. Cette documentation reflète les manifestations tant esthétiques que pragmatiques de cette culture, soit les us et coutumes, les légendes, les contes, les chansons, les métiers, le costume, la religion, la musique, les histoires de vie, etc. Elle se base principalement sur des enquêtes sur le terrain mais aussi sur des dépouillements bibliographiques et des travaux de recherche.",
            "conservation_site" : "Poitiers",
            "comment" : "",
        }
        
        verify_data(browser,data)

        # And, then logout (if authenticated user)
        if profile[0] :
            francoralite_selenium_context.logout(browser, profile[1])

def test_fonds_add(francoralite_selenium_context):
    # Go to the home page
    browser = francoralite_selenium_context.homepage(auth=True)

    # Click on the institution menu
    link_page = browser.find_element(By.XPATH, '//a[text()="' + _("Institutions") + '"]')
    link_page.click()

    # Verify the label "Institutions"
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Institutions")

    # Click on the fonds link
    link_fonds = browser.find_element(By.XPATH, '//a[text()="Université de Poitiers"]')
    link_fonds.click()

    # Verify the label of the fonds page
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Institution : Université de Poitiers")

    # Click on the "add" link
    link_add = browser.find_element(By.XPATH, '//a[text()="' + _("Créer un fonds") + '"]')
    link_add.click()

    # Write content
    content = {
        "code_partner" : "TEST 000",
        "title" : "Fonds de test",
        "conservation_site" : "Lieu test",
    }

    for key, value in content.items():
        browser.find_element(By.ID, 'id_'+ key).send_keys(value)

    code = "upoi_tst"
    browser.execute_script("document.getElementById('id_code').value='" + code + "'")
    description = 'Ceci est un fonds de test.'
    browser.find_element(By.XPATH, "//div[contains(@class, 'ProseMirror')]").send_keys(description)
    
    comment = "Un beau commentaire."
    browser.execute_script("document.getElementById('id_comment').value='" + comment + "'")
    
    content["code"] = code.upper()
    content["description"] = description
    content["comment"] = comment

    # Validation
    button_valid = browser.find_element(By.XPATH, "//*[@id='save']")
    button_valid.click()

    # Go to the new fonds
    browser = francoralite_selenium_context.get_url('/fond/3')

    verify_data(browser, content)
