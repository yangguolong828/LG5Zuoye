import yaml
from selenium.webdriver.common.by import By

from test_appium.test_frame_ymal.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.run_step("../page/search_page.yaml")
        return True
