from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.page.base_page import BasePage
from test_appium.test_appium_po.page.memberInvite_page import MemberInvitePage


class ContactPage(BasePage):

    def goto_memberinvite(self):
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)