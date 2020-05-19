from app.base.BasePage import Basepage
import allure

class personalInfo(Basepage):
    def addcomment(self):
        pass

    def sendmessage(self):
        with allure.step("点击发消息"):
            self.find("xpath",'//*[@text="发消息"]').click()
            from app.base.chatwindow import chatWindow
            return chatWindow(self._driver)

    def moreinfo(self):
        with allure.step("点击右上角更多"):
            self.find("id","com.tencent.wework:id/guk").click()
            from app.base.personalinfo2 import personalInfo2
            return personalInfo2(self._driver)
