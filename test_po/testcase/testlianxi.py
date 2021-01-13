from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class TestLianxi(BasePage):
    def test_add_department(self):
        self.driver.find_element(By.XPATH, "//*[@class='js_create_party']").click()
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("质量保障")
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='688851053681111_anchor']").click()