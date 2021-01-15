
from test_po.page.main_page import MainPage


class TestAddDepartment():

    def setup_class(self):
        # 实例化contact类
        self.main = MainPage()

    # def teardown_method(self):
    #     if __name__ == '__main__':
    #         self.main.quit()

    def test_add_department(self):
        result_deparments = self.main.goto_department().add_department().get_departmentlist()
        assert "质量保障" in result_deparments

    def test_add_sdepartment(self):
        result_sdepartments = self.main.goto_department().add_sdepartment().get_sdepartmentlist()
        assert "测试11" in result_sdepartments

