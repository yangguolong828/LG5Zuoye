from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.page.base_page import BasePage
from test_appium.test_appium_po.page.contact_page import ContactPage


# 点击通讯录
class MainPage(BasePage):

    def goto_contact(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return ContactPage(self.driver)