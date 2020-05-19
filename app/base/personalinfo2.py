from app.base.BasePage import Basepage
import allure

class personalInfo2(Basepage):
    def editmember(self):
        with allure.step("点击编辑成员"):
            self.find("xpath", "//*[@text='编辑成员']").click()
            from app.base.editmember import editMember
            return editMember(self._driver)
