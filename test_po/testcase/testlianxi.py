import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class TestLianxi():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_add_department(self):

        self.driver.get("https://work.weixin.qq.com/")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(15)
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_dropdown").click()
        self.driver.find_element(By.XPATH, "//*[@class='js_create_party']").click()
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys("质量保障")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jstree jstree-5.jstree-default [id='688851053681111_anchor']").click()
        sleep(15)
