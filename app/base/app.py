from appium import webdriver

from app.base.BasePage import Basepage
from app.base.main import Main


class App(Basepage):
    def start(self):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"
        # 官方文档：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
        if self._driver is None:
            caps = {}
            # noReset 不重启app
            caps['noReset'] = 'true'
            # skipDeviceInitialization 跳过设备初始化，包括安装和运行,可提升运行速度
            # caps['skipDeviceInitialization'] = 'true'
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = _package
            caps['appActivity'] = _activity
            caps['dontStopAppOnReset'] = 'true'
            caps['autoGrantPermissions'] = 'true'  # 自动授权
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self._driver.implicitly_wait(5)

        else:
            self._driver.start_activity(_package, _activity)

        return self

    def main(self):
        return Main(self._driver)
