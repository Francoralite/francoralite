from selenium import webdriver
from selenium.webdriver.common.by import By


def setup():
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.firefox_path = "/usr/bin/firefox-esr"
    driver = webdriver.Firefox(options=options)

    return driver

def test_homepage():
    browser = setup()
    
    # Test title
    browser.get("http://127.0.0.1:8000/")
    assert "Francoralité" in browser.title

    # Test menu
    menu = browser.find_element(By.CLASS_NAME, "menu")
    menu_list = menu.find_elements(By.TAG_NAME, 'li')
    control = {
        1 :"Institutions",
        2 :"Archives\nFonds\nMissions\nEnquêtes\nItems",
        7 :"Personnes\nEnquêteurs\nInformateurs\nAuteurs\nCompositeurs\nEditeurs",
    }
    for k,v in control.items():
        assert menu_list[k].text == v
    
    browser.quit()
