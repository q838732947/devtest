import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWeworkPytest:
    def setup(self):
        desired_caps = {}
        # noReset
        desired_caps['noReset'] = 'true'
        # skipDeviceInitialization 跳过设备初始化，包括安装和运行,可提升运行速度
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    @pytest.mark.parametrize("name,words", [
        ("陈灵", "hello"),
        ("周灵芝", "hi")
    ])
    def test_case(self, name, words):
        """
        打开企业微信（提前登录）
        进入通讯录
        点击搜索按钮
        输入 已存在的联系人姓名, 例如“aa”，
        点击联系人，进入聊天页面
        输入“测试code”
        点击发送
        退出应用
        :return:
        """
        # 使用显示等待加载首屏
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@text='通讯录']")))
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guu").click()
        # 输入搜索名字
        self.driver.find_element_by_id("com.tencent.wework:id/fk1").send_keys(f"{name}")
        # 点击第一个搜索内容
        self.driver.find_element_by_id("com.tencent.wework:id/d2f").click()
        # 点击发消息
        self.driver.find_element_by_id("com.tencent.wework:id/abo").click()
        # 输入聊天内容
        self.driver.find_element_by_id("com.tencent.wework:id/dx1").send_keys(f"{words}")
        # 点击发送
        self.driver.find_element_by_id("com.tencent.wework:id/dwx").click()
