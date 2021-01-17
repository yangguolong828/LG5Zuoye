
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存，启动app
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲时间为0秒
        caps['settings[waitForIdleTimeout]']  = 0


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def test_add_member(self):
        name = '张山'
        gender = '男'
        phonenumber = '13212324123'
        mail = "14231423@126.com"
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.find(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        if gender == '女':
            self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        else:
            self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/boh"]//*[@text="男"]').click()
        self.find(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(phonenumber)
        self.find(MobileBy.XPATH, '//*[contains(@text, "邮箱")]/../android.widget.EditText').send_keys(mail)
        self.find(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        result = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert result == "添加成功"