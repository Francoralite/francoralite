from selenium.webdriver.common.by import By
from django.utils.translation import gettext as _


def verify_data(browser, data):
    # Verify data
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == data["title"]

    label = browser.find_element(By.XPATH,  "//*[@id='id_first_name']")
    assert label.text == data["first_name"]

    label = browser.find_element(By.XPATH, "//*[@id='id_last_name']")
    assert label.text == data["last_name"]

    label = browser.find_element(By.XPATH, "//*[@id='id_civility']")
    assert label.text == data["civility"]

    label = browser.find_element(By.XPATH, "//*[@id='id_alias']")
    assert label.text == data["alias"]

    label = browser.find_element(By.XPATH, "//*[@id='id_birth_date']")
    assert label.text == data["birth_date"]
    label = browser.find_element(By.XPATH, "//*[@id='id_birth_location']")
    assert label.text == data["birth_location"]

    label = browser.find_element(By.XPATH, "//*[@id='id_death_date']")
    assert label.text == data["death_date"]
    label = browser.find_element(By.XPATH, "//*[@id='id_death_location']")
    assert label.text == data["death_location"]

    label = browser.find_element(By.XPATH, "//*[@id='id_biography']")
    assert label.text == data["biography"]

    label = browser.find_element(By.XPATH, "//*[@id='id_uri']")
    assert label.text == data["uri"]

def test_authority_details(francoralite_selenium_context, all_profiles):
    
    # Open the homepage for each profile 
    for profile in all_profiles:
        francoralite_selenium_context.homepage(auth=profile[0], username=profile[1])
        browser = francoralite_selenium_context.get_url("/authority/1")

        # Verify data
        data = {
            "title" : "Personne : Le Gaulois Astérix",
            "last_name" : "Le Gaulois",
            "first_name" : "Astérix",
            "civility" : "",
            "alias" : "",
            "birth_date" : "",
            "birth_location" : "",
            "death_date" : "",
            "death_location" : "",
            "biography" : "",
            "uri" : "",
        }
        
        verify_data(browser,data)

        # And, then logout (if authenticated user)
        if profile[0] :
            francoralite_selenium_context.logout(browser, profile[1])
        

def test_authority_add(francoralite_selenium_context):
    # Go to the home page
    browser = francoralite_selenium_context.homepage(auth=True)

    # Click on authority menu
    browser.find_element(By.XPATH, '//a[text()="' + _("Personnes") + '"]').click()

    # On authority list
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Personnes")

    # Click on the "add" link
    browser.find_element(By.XPATH, '//a[contains(@href,"/authority/add")]').click()

    # Write content
    content = {
        "last_name" : "verne",
        "first_name" : "jules",
        "alias" : "julot",
        "civility" : "mr",
        "birth_date" : "1828-02-08",
        "death_date" : "1905-03-24",
        "uri" : "https://fr.wikipedia.org/wiki/Jules_Verne",
    }
    biography = "Jules Verne, né le 8 février 1828 à Nantes et mort le 24 mars 1905 à Amiens, est un écrivain français"

    for key, value in content.items():
        browser.find_element(By.ID, 'id_'+ key).send_keys(value)

    browser.find_element(By.XPATH, "//div[contains(@class, 'ProseMirror')]").send_keys(biography)

    # Validation
    button_valid = browser.find_element(By.XPATH, "//*[@id='save']")
    button_valid.click()

    # Go to the new authority
    browser = francoralite_selenium_context.get_url('/authority/8')

    # Verify data
    content["title"] = "Personne : verne jules"
    content["biography"] = biography
    content["birth_location"] = ""
    content["death_location"] = ""
        
    verify_data(browser, content)
   