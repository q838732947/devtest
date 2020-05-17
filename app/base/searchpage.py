from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.base.BasePage import Basepage


class searchPage(Basepage):
    def searchtext(self, searchtext):
        self.find('id', "com.tencent.wework:id/fk1").send_keys(f"{searchtext}")
        WebDriverWait(self._driver, 5).until(expected_conditions.invisibility_of_element_located(("xpath", "联系人")))
        return self

    def pointfirstresult(self):
        self.find('id', 'com.tencent.wework:id/d2f').click()
        from app.base.personalinfo import personalInfo
        return personalInfo(self._driver)

    def back(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/gu_").click()
        print("点击返回按钮")
        from app.base.Address import Address
        return Address(self._driver)