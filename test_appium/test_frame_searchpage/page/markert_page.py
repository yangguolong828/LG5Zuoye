from selenium.webdriver.common.by import By

from test_appium.test_frame_searchpage.base_page import BasePage
from test_appium.test_frame_searchpage.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find_and_click((By.ID, "com.xueqiu.android:id/action_search"))
        return SearchPage(self.driver)