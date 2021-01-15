from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage

from test_po.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):

    #添加部门成功
    def add_department(self):
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("质量保障")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_party_list_container [id="1688851053681111_anchor"]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_foot a:nth-child(1)").click()
        return ContactPage(self.driver)

    #添加子部门成功
    def add_sdepartment(self):
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("测试11")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_party_list_container [id="1688850854889588_anchor"]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_foot a:nth-child(1)").click()
        return ContactPage(self.driver)
