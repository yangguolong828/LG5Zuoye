import pytest

from test_request.api.contact import Contact


class TestContact:
    def setup(self):
        self.contact = Contact()

    @pytest.mark.parametrize("userid,mobile", [("ceshi1", "13243213211"),
                                               ("ceshi2", "13243213212"),
                                               ("ceshi3", "13243213213")])
    def test_add_member(self, userid, mobile):
        name = "member1"
        department = [1]
        # 数据清理
        self.contact.delete_member(userid)
        # 添加成员
        r_add = self.contact.add_member(userid=userid, mobile=mobile,department=department,name=name)
        assert r_add.get("errcode") == 0
        # 查询成员
        r = self.contact.get_member(userid)
        assert r.get("name") == name