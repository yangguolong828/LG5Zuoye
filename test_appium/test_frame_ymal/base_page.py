import yaml
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium.test_frame_ymal.handle_black import handle_black


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

    def send(self, locator, content):
        self.find(locator).send_keys(content)

    def run_step(self, page_path):
        with open(page_path, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        for step in data:
            action = step['action']
            if action == "find_and_click":
                self.find_and_click(step['locator'])
            elif action == "send":
                self.send(step['locator'], step['content'])

