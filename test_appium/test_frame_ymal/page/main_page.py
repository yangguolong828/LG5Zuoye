import yaml

from test_appium.test_frame_ymal.base_page import BasePage
from test_appium.test_frame_ymal.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.run_step("../page/main_page.yaml", "goto_market_page")
        return MarketPage(self.driver)