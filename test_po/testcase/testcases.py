from test_po.page.contact_page import ContactPage
from test_po.page.main_page import MainPage


class TestAddDepartment():

    def setup_class(self):
        # 实例化main类
        self.contact = ContactPage
        self.main = MainPage

    def test_add_department(self):
        self.contact.goto_add_department(self).add_department()