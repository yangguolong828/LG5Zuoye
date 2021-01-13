from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
# from test_po.page.contact_page import ContactPage
# from test_po.page.contact_page_new import NewContactPage


class AddDepartmentPage(BasePage):

    #添加部门成功
    def add_department(self):
        self.driver.find_element(By.XPATH, "//*[@class='js_create_party']").click()
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("质量保障")
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='688851053681111_anchor']").click()


    #添加部门失败
    def add_department_fail(self):
        pass

    #添加子部门成功
    def add_sdepartment(self):
        pass

    #添加子部门失败
    def add_sdepartment_fail(self):
        pass