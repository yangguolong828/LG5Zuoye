from selenium import webdriver


class BasePage():

    def base_webdriver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
