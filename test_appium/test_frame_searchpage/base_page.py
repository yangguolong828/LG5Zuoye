
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium.test_frame_searchpage.handle_black import handle_black


class BasePage:


    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_by(self, by, value):
        return self.driver.find_element(by=by,value=value)

    @handle_black
    def find(self, locator):
            return self.driver.find_element(*locator)


    def find_and_click(self, locator):
        self.find(locator).click()

