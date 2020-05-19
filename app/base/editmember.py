from app.base.BasePage import Basepage
import allure

class editMember(Basepage):
    def delMember(self):
        with allure.step("滚动查找删除成员安宁并点击弹窗中的确定按钮"):
            self.rollfind_bytext("删除成员").click()
            self.find("xpath", "//*[@text='确定']").click()
            from app.base.searchpage import searchPage
            return searchPage(self._driver)
