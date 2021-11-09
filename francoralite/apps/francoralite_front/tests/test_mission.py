from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from django.utils.translation import gettext as _

def verify_data(browser, data):
    # Verify data
 
    label = browser.find_element(By.XPATH,  "//*[@id='id_code']")
    assert label.text == data["code"]

    try:
        label = browser.find_element(By.XPATH,  "//*[@id='id_code_partner']")
    except Exception as e:
        pass
    else:
        assert label.text == data["code_partner"]

    label = browser.find_element(By.XPATH, "//*[@id='id_title']")
    assert label.text == data["title"]

    label = browser.find_element(By.XPATH, "//*[@id='id_description']")
    assert label.text == data["description"]
    
def test_mission_list(francoralite_selenium_context, all_profiles):
    for profile in all_profiles:
        francoralite_selenium_context.homepage(auth=profile[0], username=profile[1])
        browser = francoralite_selenium_context.get_url("/mission")

         # Verify the label of the mission page
        label = browser.find_element(By.XPATH, "//main/h1")
        assert label.text == _("Missions")

        # links to the missions
        link_view_1 = browser.find_element(By.XPATH, '//a[@href="/mission/1"]')
        assert link_view_1.text == "UPOI_AFE_0000"

        link_view_2 = browser.find_element(By.XPATH, '//a[@href="/mission/2"]')
        assert link_view_2.text == "UPOI_ATP_0000"

        if(profile[0]=="contributeur"):
            assert browser.find_element(By.XPATH, '//a[@href="/mission/edit/1"]')
            assert browser.find_element(By.XPATH, '//a[@href="/mission/edit/2"]')
            assert browser.find_element(By.XPATH, '//button[@data-url="/mission/delete/1"]')
            assert browser.find_element(By.XPATH, '//button[@data-url="/mission/delete/2"]')

def test_fonds_details(francoralite_selenium_context, all_profiles):
    # Open the homepage for each profile 
    for profile in all_profiles:
        francoralite_selenium_context.homepage(auth=profile[0], username=profile[1])
        browser = francoralite_selenium_context.get_url("/mission/1")

        # Verify data
        data = {
            "title": "Extraits d'enquêtes du fonds Archives de Folklore et d'Ethnologie [Exemple]",
            "description": "Sélection de copies commandées par Joseph Le Floc'h en 1994 aux Archives de Folklore de l'Université Laval, pour ses cours sur la chanson de tradition orale franco-canadienne au Département de Musicologie de l'Université de Poitiers.\nLes Archives de folklore et d'ethnologie sont constituées des fonds et des collections, privés ou publics, concernant la culture des francophones en Amérique du Nord. Cette documentation reflète les manifestations tant esthétiques que pragmatiques de cette culture, soit les us et coutumes, les légendes, les contes, les chansons, les métiers, le costume, la religion, la musique, les histoires de vie, etc. Elle se base principalement sur des enquêtes sur le terrain mais aussi sur des dépouillements bibliographiques et des travaux de recherche.",
            "code": "UPOI_AFE_0000",
        }
        
        verify_data(browser,data)

        # And, then logout (if authenticated user)
        if profile[0] :
            francoralite_selenium_context.logout(browser, profile[1])

def test_mission_add(francoralite_selenium_context):
    # Go to the fonds page
    francoralite_selenium_context.homepage(auth=True)
    browser = francoralite_selenium_context.get_url("/fond/1")
    
     # Verify the label of the fonds page
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == _("Fonds : Fonds issus des Archives de Folklore et d'Ethnologie [Exemple]")

    # Click on the "add" link
    link_add = browser.find_element(By.XPATH, '//a[@href="/institution/1/fond/1/mission/add"]')
    link_add.click()

    # Write content
    content = {
        "code_partner" : "TEST 000",
        "title" : "Mission de test",
        "public_access" : "full"
    }

    for key, value in content.items():
        browser.find_element(By.ID, 'id_'+ key).send_keys(value)

    # Write special content
    code = "upoi_afe_0001"
    browser.execute_script("document.getElementById('id_code').value='" + code + "'")
    content["code"] = code.upper()

    description = 'Ceci est une mission de test.'
    browser.find_element(By.XPATH, "//div[contains(@class, 'ProseMirror')]").send_keys(description)
    content["description"] = description

    # Validation
    button_valid = browser.find_element(By.XPATH, "//*[@id='save']")
    button_valid.click()

    # Go to the new fonds
    browser = francoralite_selenium_context.get_url('/mission/4')
 
    verify_data(browser, content)
