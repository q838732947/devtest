from app.base.BasePage import Basepage


class personalInfo(Basepage):
    def addcomment(self):
        pass

    def sendmessage(self):
        self.find("xpath",'//*[@text="发消息"]').click()
        from app.base.chatwindow import chatWindow
        return chatWindow(self._driver)

    def moreinfo(self):
        self.find("id","com.tencent.wework:id/guk").click()
        from app.base.personalinfo2 import personalInfo2
        return personalInfo2(self._driver)
