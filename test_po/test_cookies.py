import json

from selenium import webdriver


class Testcookies():

    def setup(self):
        chrome_arges = webdriver.ChromeOptions()
        chrome_arges.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_arges)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        cookies = self.driver.get_cookies()

        with open("cookies.json", "w") as f:
            json.dump(cookies,f)