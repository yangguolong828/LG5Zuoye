from time import sleep

from selenium.webdriver.common.by import By
from test_po.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def goto_add_department(self):
        pass

    def get_memberlist(self):
        pass

    def get_departmentlist(self):
        """
        返回通讯录页面的组织架构信息
        :retrun:
        """
        department_webele_list = self.driver.find_elements(By.XPATH, '//*[@class="jstree-anchor"]')
        department_list = []
        for webelement in department_webele_list:
            department_list.append(webelement.text)

        # 返回department_list数据
        return department_list

    def get_sdepartmentlist(self):
        """
        返回通讯录页面的子组织架构信息
        :retrun:
        """
        self.find(By.XPATH, '//*[@id="1688850854889588_anchor"]')
        sdepartment_webele_list = self.driver.find_elements(By.XPATH, '//*[@id="1688850854889588"]/ul')
        sdepartment_list = []
        for webelement in sdepartment_webele_list:
            sdepartment_list.append(webelement.text)

        # 返回department_list数据
        return sdepartment_list
