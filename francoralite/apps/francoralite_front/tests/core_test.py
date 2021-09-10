from selenium import webdriver


class CoreTest():
    def __init__(self):
        self.URL = "http://127.0.0.1:8000/"
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.firefox_path = "/usr/bin/firefox-esr"
        self.driver = webdriver.Firefox(options=options)

    def homepage(self):
        self.driver.get(self.URL)
