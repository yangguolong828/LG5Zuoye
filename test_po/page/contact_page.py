from selenium.webdriver.common.by import By

from test_po.page.add_department_page import AddDepartmentPage
from test_po.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def goto_add_department(self):
        #查找元素进入添加组织弹窗
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_dropdown").click()
        #返回AddDepartmentPage
        return AddDepartmentPage(self.driver)

    def get_memberlist(self):
        pass

    def get_departmentlist(self):
        pass
