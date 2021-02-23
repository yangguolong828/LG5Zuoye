import requests

class TestContact():

    def test_request(self):

        # 获取token
        url_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8d11df16a0576625&corpsecret=go2w1K994D5FO24xp-bMQbTTBwz2YbvJAJexdf0cRYw"
        r_token = requests.get(url_token)
        token = r_token.json()['access_token']

        # 读取成员
        url_get = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=YangGuoLong"
        r_get = requests.get(url_get)
        print(r_get.json())

        # 新建通讯录成员
        url_add = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        body = {
            "userid": "ceshi12345",
            "name": "测试12345",
            "mobile": "+86 13200000200",
            "department": [1]
        }
        r_add = requests.post(url_add, json=body)
        result = r_add.json()['errcode']
        if result == 0:
            print("新建成员成功")
        else:
            print(r_add.json())

        # 更新通讯录成员
        url_update = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
        body = {
            "userid": "ceshi1234",
            "name": "测试123"
        }
        r_update = requests.post(url_update, json=body)
        result = r_update.json()['errmsg']
        if result == "updated":
            print("更新成员成功")
        else:
            print(r_update.json())
        # 删除通讯录成员
        url_delete = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=ceshi12345"
        r_delete = requests.get(url_delete)
        result = r_delete.json()['errmsg']
        if result == "deleted":
            print("删除成员成功")
        else:
            print(r_delete.json())