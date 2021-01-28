from selenium.webdriver.common.by import By

from test_appium.test_frame_searchpage.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        with open("../page/main_page.yaml", "r", encoding="utf-8") as f:
            data = yaml.load(f)
        for step in data:
            action = step["action"]
            if action == "find_and_click":
                self.find_and_click("locator")
        # self.find_by(By.XPATH, ).send_keys("阿里巴巴")
        # self.find_and_click((By.XPATH, ))
        return True
