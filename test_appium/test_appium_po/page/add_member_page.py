from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.test_appium_po.page.base_page import BasePage


# 编辑成员的信息
class AddMemberPage(BasePage):

    def edit_name(self, name):
        self.find_by(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        return self
    def edit_gender(self, gender):
        locator = (MobileBy.XPATH, '//*[@text="男"]')
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        ele.click()

        if gender == '女':
            self.find_and_click((MobileBy.XPATH, '//*[@text="女"]'))
        else:
            self.find_and_click((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/boh"]//*[@text="男"]'))
        return self
    def edit_phonenum(self, phonenum):
        self.find_by(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(phonenum)
        return self
    def click_save(self):
        from test_appium.test_appium_po.page.memberInvite_page import MemberInvitePage
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/ie7"))
        return MemberInvitePage(self.driver)