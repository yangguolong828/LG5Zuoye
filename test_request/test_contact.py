import requests

class TestContact():
    def setup(self):
        # 获取token
        url_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8d11df16a0576625&corpsecret=go2w1K994D5FO24xp-bMQbTTBwz2YbvJAJexdf0cRYw"
        r_token = requests.get(url_token)
        token = r_token.json()['access_token']
