from app.base.Address import Address
from app.base.BasePage import Basepage


class Main(Basepage):
    def goto_tab2(self):
        self.steps("../base/main.yaml")
        # self.find("xpath", "//*[@text='通讯录']").click()
        return Address(self._driver)

    def goto_tab3(self):
        pass

    def goto_tab4(self):
        pass
