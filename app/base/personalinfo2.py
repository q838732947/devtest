from app.base.BasePage import Basepage


class personalInfo2(Basepage):
    def editmember(self):
        self.find("xpath", "//*[@text='编辑成员']").click()
        from app.base.editmember import editMember
        return editMember(self._driver)
