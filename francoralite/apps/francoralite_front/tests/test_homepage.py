from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_homepage(francoralite_selenium_context):
    browser = francoralite_selenium_context.homepage()

    # Test title
    assert "Francoralité" in browser.title

    # Test menu
    menu = browser.find_element(By.CLASS_NAME, "menu")
    menu_list = menu.find_elements(By.XPATH, '//li[not(ancestor::li/ul)]')

    control = {
        "Accueil" : 0,
        "Institutions" : 1,
        "Archives" : 2,
        "Personnes" : 3,
        "Enumérations" : 4,
        "Lieux" : 5,
        "Recherche avancée" : 6,
    }

    for k,v in control.items():
        assert menu_list[v].text == k


    # Click on each menu item
    data = [
        ["Institutions"],
        ["Archives",["Fonds", "Missions", "Enquêtes", "Items"] ],
        ["Personnes", ["Enquêteurs", "Informateurs", "Auteurs", "Compositeurs", "Editeurs"] ],
        ["Lieux", [["Par enquêtes", "Lieux, par enquêtes"]] ]
        ]
    
    for item in data :
       
        if len(item) == 1 :
            goto_page(browser, item[0])   
        else :
            topic = item[0]
            for element in item[1] :
                a = ActionChains(browser)
                topic_link = browser.find_element(By.XPATH, '//a[text()="' + topic + '"]')
                
                # Move the mouse to the topic link
                a.move_to_element(topic_link).perform()

                goto_page(browser,element)

def goto_page(browser,link):

    # It's list (link different of target)
    if isinstance(link,list):
        target = link[1]
        link = link[0]
    else:
        target = link

    # Goto to the linked page
    link_page = browser.find_element(By.XPATH, '//a[text()="' + link + '"]')
    a = ActionChains(browser)
    a.move_to_element(link_page).perform()
    link_page.click()
    label = browser.find_element(By.XPATH, "//main/h1")
    
    # Test the right label
    assert label.text == target
