import yaml
from selenium.webdriver.common.by import By

from test_appium.test_frame_searchpage.base_page import BasePage
from test_appium.test_frame_searchpage.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        with open("../page/market_page.yaml", 'r', encoding="utf-8") as f:
            data = yaml.load(f)
        for step in data:
            action = step['action']
            if action == "find_and_click":
                self.find_and_click(step['loactor'])
        return SearchPage(self.driver)