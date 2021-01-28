import yaml

from test_appium.test_frame_searchpage.base_page import BasePage
from test_appium.test_frame_searchpage.page.markert_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        with open("../page/main_page.yaml", "r", encoding="utf-8") as f:
            data = yaml.load(f)
        for step in data:
            action = step["action"]
            if action == "find_and_click":
                self.find_and_click("locator")
        return MarketPage(self.driver)