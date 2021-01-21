from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.page.add_member_page import AddMemberPage
from test_appium.test_appium_po.page.base_page import BasePage

# 点击手动添加
class MemberInvitePage(BasePage):

    def goto_add_member(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return AddMemberPage(self.driver)

    def get_toast(self):
        result = self.find_and_get_text((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        return result