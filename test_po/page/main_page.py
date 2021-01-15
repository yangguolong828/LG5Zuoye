from selenium.webdriver.common.by import By

from test_po.page.add_department_page import AddDepartmentPage
from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_add_member(self):
        pass

    def goto_department(self):
        # 进入通讯录页面
        self.find(By.ID, "menu_contacts").click()
        # 定位+按钮
        self.find(By.CSS_SELECTOR, ".js_create_dropdown").click()
        # 定位部门，进入添加部门弹窗
        self.find(By.XPATH, "//*[@class='js_create_party']").click()
        return AddDepartmentPage(self.driver)

