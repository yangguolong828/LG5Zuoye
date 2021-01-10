import json

from selenium import webdriver
# import collections.abc
# print(isinstance('hello',collections.abc.Iterable)) #判断是否可以迭代

class Testcookies():

    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        #获取cookie
        cookies = self.driver.get_cookies()
        # 以文件流的形式打开文件
        with open("cookie.json", "w") as f:
            # 存储cookie到文件中
            json.dump(cookies,f)