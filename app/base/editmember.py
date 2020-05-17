from app.base.BasePage import Basepage


class editMember(Basepage):
    def delMember(self):
        self.rollfind_bytext("删除成员").click()
        self.find("xpath", "//*[@text='确定']").click()
        from app.base.searchpage import searchPage
        return searchPage(self._driver)
