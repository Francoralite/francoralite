from selenium.webdriver.common.by import By
from django.utils.translation import gettext as _


def verify_data(browser, data):
    # Verify data

    for key, value in data.items():
        label = browser.find_element(By.XPATH,  "//*[@id='id_" + key + "']")
        assert label.text == value
        
def test_collection_list(francoralite_selenium_context, all_profiles):
    for profile in all_profiles:
        francoralite_selenium_context.homepage(auth=profile[0], username=profile[1])
        browser = francoralite_selenium_context.get_url("/collection")
        
         # Verify the label of the collection page
        label = browser.find_element(By.XPATH, "//main/h1")
        assert label.text == _("Enquêtes")
        
        # links to the collections
        link_view_1 = browser.find_element(By.XPATH, '//a[@href="/collection/1"]')
        assert link_view_1.text == "UPOI_AFE_0000_0001"
        
        link_view_2 = browser.find_element(By.XPATH, '//a[@href="/collection/2"]')
        assert link_view_2.text == "UPOI_ATP_0001_0001"
        
        if(profile[0]=="contributeur"):
            assert browser.find_element(By.XPATH, '//a[@href="/collection/edit/1"]')
            assert browser.find_element(By.XPATH, '//a[@href="/collection/edit/2"]')
            assert browser.find_element(By.XPATH, '//button[@data-url="/collection/delete/1"]')
            assert browser.find_element(By.XPATH, '//button[@data-url="/collection/delete/2"]')

def test_collection_details(francoralite_selenium_context, all_profiles):
    # Open the homepage for each profile
    for profile in all_profiles:
        francoralite_selenium_context.homepage(auth=profile[0], username=profile[1])
        browser = francoralite_selenium_context.get_url("/collection/1")

        # Verify data
        data = {
            "title": "Répertoire chanté de Sœur Cécilia McGraw au Nouveau-Brunswick [Extrait d'enquête]",
            "description": "Extrait d'enquête de Sœur Jeanne d'Arc Lortie le 15 mars 1963 auprès de Sœur Cécilia McGraw (53 ans).",
            "code": "UPOI_AFE_0000_0001",
            "recorded_from_year": "1963-01-01",
            "recorded_to_year": "1963-01-02",
            "year_published": "",
            "legal_rights": "domaine public",
        }

        verify_data(browser, data)

        # And, then logout (if authenticated user)
        if profile[0]:
            francoralite_selenium_context.logout(browser, profile[1])

def test_collection_add(francoralite_selenium_context):
    # Go to the collection page
    francoralite_selenium_context.homepage(auth=True)
    browser = francoralite_selenium_context.get_url("/mission/1")

    # Verify the label of the collection page
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Mission : Extraits d'enquêtes du fonds Archives de Folklore et d'Ethnologie [Exemple]")

    # Click on the "add" link
    link_add = browser.find_element(By.XPATH, '//a[@href="/institution/1/fond/1/mission/1/collection/add"]')
    link_add.click()

    # Write content
    content = {
        "title": "Collection test",
        "recorded_from_year": "1995-01-01",
        "recorded_to_year": "2015-01-02",
        "year_published": 2021,
        "legal_rights": "domaine public",
    }

    for key, value in content.items():
        browser.find_element(By.ID, 'id_' + key).send_keys(value)

    # Write special content
    code = "upoi_afe_0000_0002"
    browser.execute_script("document.getElementById('id_code').value='" + code + "'")
    content["code"] = code.upper()

    description = 'Ceci est une collection de test.'
    browser.find_element(By.XPATH, "//div[contains(@class, 'ProseMirror')]").send_keys(description)
    content["description"] = description

    year_published = '2021'
    browser.execute_script("document.getElementById('id_year_published').value='" + year_published + "'")
    content["year_published"] = year_published

    # Validation
    button_valid = browser.find_element(By.XPATH, "//*[@id='save']")
    button_valid.click()

    # Go to the new collection
    browser = francoralite_selenium_context.get_url('/collection/3')

    # Take a screenshot for debug
    # browser.save_screenshot('./page.png')

    verify_data(browser, content)
