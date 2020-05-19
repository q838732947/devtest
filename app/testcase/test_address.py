from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAddress:
    #不使用PO模式编写
    def setup_class(self):
        desired_caps = {}
        # noReset
        desired_caps['noReset'] = 'true'
        # skipDeviceInitialization 跳过设备初始化，包括安装和运行,可提升运行速度
        # desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        # self.driver.quit()
        pass

    @pytest.mark.parametrize("name, gender, phonenum", [
        ("测试name5", "女", "18600000005"),
        ("测试name6", "女", "18600000006")
    ])
    def test_addconnect(self, name, gender, phonenum):
        """
        添加联系人的姓名以固定字符开头，例如：测试name1，测试name2，测试name3
         """
        # 使用显示等待加载首屏
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@text='通讯录']")))
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找 添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                               'new UiSelector().scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector().text("添加成员")'
                                                               '.instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"姓名")]/..//*[@resource-id="com.tencent.wework:id/au0"]').send_keys(
            f"{name}")

        # 点击性别
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/av2").click()
        # 选择男女
        print(f'//*[@resource-id="com.tencent.wework:id/dqn"and @text="{gender}"]')
        sleep(1)
        self.driver.find_element(MobileBy.XPATH,
                                 f'//*[@resource-id="com.tencent.wework:id/dqn"and @text="{gender}"]').click()
        # 输入手机号
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/eq7"]').send_keys(
            f"{phonenum}")
        # 点击保存
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gur"]').click()
        # toast提示添加成功
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

    # 输入手机号
    def test_delconnect(self):
        """
        循环删除所有 "测试name"开头的联系人
        删除联系人之后，判断删除成功
        """
        # 使用显示等待加载首屏
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@text='通讯录']")))
        # 点击通讯录
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 找出所有name符合条件的list

        while True:
            eles: list = self.driver.find_elements(MobileBy.XPATH, '//*[contains(@text,"测试name")]')
            if len(eles) > 0:
                delname = eles[0].text
                # 点击待删除成员名字
                self.driver.find_element(MobileBy.XPATH, f'//*[contains(@text,"{delname}")]').click()
                # 点击右上角
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guk").click()
                sleep(3)
                # 点击编辑成员
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/azd").click()
                sleep(3)
                # 滚动查找，点击删除成员
                self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                                       'new UiSelector().scrollable(true).instance(0))'
                                                                       '.scrollIntoView(new UiSelector().text("删除成员")'
                                                                       '.instance(0));').click()
                sleep(1)
                # 点击确定
                self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
                sleep(2)
                # 点击返回
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gu_").click()
                # 等待元素消失
                sleep(3)