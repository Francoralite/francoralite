from selenium.webdriver.common.by import By


def test_homepage(francoralite_selenium_context):
    browser = francoralite_selenium_context.homepage()

    # Test title
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

    # Click on each menu item
    data = [
        "Institutions",
        "Fonds", "Missions", "Enquêtes", "Items",
        "Personnes", "Enquêteurs", "Informateurs", "Auteurs", "Compositeurs", "Editeurs",
        "Coupe", "Voix/Instruments", "Organisation musicale",
        ["Formation (musicale)", "Formation"],["Hornbostel-Sachs","classification Hornbostel-Sachs"],
        "Genre de chanson", "Genre de conte", "Genre de musique", "Genre vocal",
        "Contexte d'enregistrement",
        "Droits légaux", "Éditeur", "Meta donnée auteur", "Type de média",
        ["Danse","Genre de danse"],
        "Langue",
        "Thématique",
        "Fonction",
        "Lieux", ["Par enquêtes", "Lieux, par enquêtes"]
        ]

    for item in data :
        link = item
        target = item
        if isinstance(item,list):
            link = item[0]
            target = item[1]

        link_institution = browser.find_element(By.LINK_TEXT, link)
        link_institution.click()
        label = browser.find_element(By.XPATH, "//main/h1")
        assert label.text == target
