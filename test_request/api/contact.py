from test_request.api.base import Base


class Contact(Base):

    # 添加通讯录成员
    def add_member(self, userid: str, name: str, mobile: str, department: list, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        body.update(kwargs)
        return self.send("post", url, json=body)


        # 读取成员
    def get_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get", url)

    # 更新通讯录成员
    def update_member(self, userid, name, **kwargs):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name
        }
        body.update(kwargs)
        return self.send("post", url, data=body)

        # 删除通讯录成员
    def delete_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get", url)