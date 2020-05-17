from appium.webdriver.common.mobileby import MobileBy

from app.base.BasePage import Basepage
from app.base.searchpage import searchPage


class Address(Basepage):
    def addmember(self):
        # self.find(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));').click()
        self.rollfind_bytext("添加成员").click()
        from app.base.addmember import addMember
        print("点击添加成员")
        return addMember(self._driver)

    def pointmember(self, name):
        pass

    def outmember(self):
        pass

    def search(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/guu").click()
        return searchPage(self._driver)
