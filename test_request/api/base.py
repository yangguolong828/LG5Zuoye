import requests


class Base:
    def __init__(self):

        # 获取token
        url_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8d11df16a0576625&corpsecret=go2w1K994D5FO24xp-bMQbTTBwz2YbvJAJexdf0cRYw"
        r = requests.get(url_token).json()
        self.token = r['access_token']
        # 声明一个session
        self.s = requests.Session()
        # 把token 放入到session  每次参数都有token
        self.s.params = {'access_token': self.token}


    def send(self, *args, **kwargs):
        r = self.s.request(*args, **kwargs)
        return r.json()