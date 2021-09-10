from selenium.webdriver.common.by import By
from .core_test import CoreTest

ct = CoreTest()
browser = ct.driver


def test_authority_details():
    browser.get(ct.URL + "authority/1")

    # Verify data
    label = browser.find_element(By.XPATH, "//main/h1")
    assert label.text == "Personne : Le Gaulois Astérix"

    label = browser.find_element(By.XPATH, "//main/div[1]/dl[1]/dd")
    assert label.text == "Astérix"

    label = browser.find_element(By.XPATH, "//main/div[1]/dl[2]/dd")
    assert label.text == "Le Gaulois"

    label = browser.find_element(By.XPATH, "//main/div[2]/dl[1]/dd")
    assert "glyphicon-ok" in label.get_attribute("class")

    label = browser.find_element(By.XPATH, "//main/div[2]/dl[2]/dd")
    assert "glyphicon-ok" in label.get_attribute("class")

    label = browser.find_element(By.XPATH, "//main/div[2]/dl[3]/dd")
    assert "glyphicon-ok" in label.get_attribute("class")
