import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWorlWechart():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_workwechart(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookie.json", "r") as f:
            #读取cookies
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]/span').click()
        sleep(3)