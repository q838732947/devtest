from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        desired_caps = {}
        # {'noReset': 'True', 'platformName': 'Android', 'platformVersion': '6.0','deviceName': 'emulator-5554', 'appPackage': 'com.xueqiu.android','appActivity': 'com.xueqiu.android.common.MainActivity'}
        # noReset
        desired_caps['noReset'] = 'true'
        # skipDeviceInitialization 跳过设备初始化，包括安装和运行,可提升运行速度
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_case(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='行情']").click()
        # sleep(2)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_search").click()
        # sleep(2)
        self.driver.find_element(MobileBy.CLASS_NAME, "android.widget.EditText").send_keys("alibaba")
        sleep(3)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        print(self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("com.xueqiu.android:id/current_price")').text)
        print(self.driver.find_element(MobileBy.XPATH,
                                       "//*[@text='BABA']/../../..//*["
                                       "@resource-id='com.xueqiu.android:id/current_price']").text)
