import yaml
from selenium.webdriver.common.by import By

from test_appium.test_frame_ymal.base_page import BasePage
from test_appium.test_frame_ymal.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_step("../page/market_page.yaml")
        return SearchPage(self.driver)