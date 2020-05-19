import allure
from appium.webdriver.common.mobileby import MobileBy

from app.base.BasePage import Basepage
from app.base.manmuladdmember import manmulAddMember


class addMember(Basepage):
    def wechat_invite(self):
        pass

    def wechatfriend_invite(self):
        pass

    def address_invite(self):
        pass

    def manual_invite(self):
        with allure.step("点击手动输入添加"):
            self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
            return manmulAddMember(self._driver)

    def back(self):
        with allure.step("点击返回按钮"):
            from app.base.Address import Address
            self.find(MobileBy.ID, "com.tencent.wework:id/gu_").click()
            return Address(self._driver)
