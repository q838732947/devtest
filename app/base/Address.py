from appium.webdriver.common.mobileby import MobileBy

from app.base.BasePage import Basepage
from app.base.searchpage import searchPage
import allure


class Address(Basepage):
    def addmember(self):
        # self.find(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));').click()
        with allure.step("滚动查找并点击添加成员"):
            self.rollfind_bytext("添加成员").click()
            from app.base.addmember import addMember
            return addMember(self._driver)

    def pointmember(self, name):
        pass

    def outmember(self):
        pass

    def search(self):
        with allure.step("点击搜索框"):
            self.find(MobileBy.ID, "com.tencent.wework:id/guu").click()
            return searchPage(self._driver)
