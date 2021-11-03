from selenium.webdriver.common.by import By
from django.utils.translation import gettext as _


def verify_data(browser, data):
    # Verify data
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == data["title"]

    label = browser.find_element(By.XPATH,  "//*[@id='id_name']")
    assert label.text == data["name"]

    label = browser.find_element(By.XPATH, "//*[@id='id_notes']")
    assert label.text == data["notes"]

def test_dance_details(francoralite_selenium_context, all_profiles):
    
    # Open the homepage for each profile 
    for profile in all_profiles:
        francoralite_selenium_context.homepage(auth=profile[0], username=profile[1])
        browser = francoralite_selenium_context.get_url("/dance/1")

        # Verify data
        data = {
            "title" : "Genre de danse : polka",
            "name" : "polka",
            "notes" : "Polka",
        }
        
        verify_data(browser,data)

        # And, then logout (if authenticated user)
        if profile[0] :
            francoralite_selenium_context.logout(browser, profile[1])
        

def test_dance_add(francoralite_selenium_context):
    # Go to the dance add page
    francoralite_selenium_context.homepage(auth=True, username="administrateur")
    browser = francoralite_selenium_context.get_url("/dance/add")

    # On page add
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Genre de danse - Création")

    # Write content
    content = {
        "name" : "bourree",
        "notes" : "Bourrée",
    }
    
    for key, value in content.items():
        browser.find_element(By.ID, 'id_'+ key).send_keys(value)

    # Validation
    button_valid = browser.find_element(By.XPATH, "//*[@id='save']")
    button_valid.click()

    # Go to the new dance
    browser = francoralite_selenium_context.get_url('/dance/2')

    # Verify data
    content["title"] = "Genre de danse : bourree"
        
    verify_data(browser, content)
   