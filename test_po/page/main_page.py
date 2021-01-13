from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_add_member(self):
        pass

    # def goto_contact(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
    #     return ContactPage(self.driver)
