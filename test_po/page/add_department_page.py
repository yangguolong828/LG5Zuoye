from selenium.webdriver.common.by import By
from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage

class AddDepartmentPage(BasePage):
    _depname = (By.XPATH, "//*[@name='name']")

    #添加部门成功
    def add_department(self,name):
        self.find(*self._depname).send_keys(name)
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR, '.js_party_list_container [id="1688851053681111_anchor"]').click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_foot a:nth-child(1)").click()
        return ContactPage(self.driver)

    #添加子部门成功
    def add_sdepartment(self,sname):
        self.find(*self._depname).send_keys(sname)
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR, '.js_party_list_container [id="1688850854889588_anchor"]').click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_foot a:nth-child(1)").click()
        return ContactPage(self.driver)
