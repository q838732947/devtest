from app.base.Address import Address
from app.base.BasePage import Basepage
import allure

class Main(Basepage):
    def goto_tab2(self):
        with allure.step("点击通讯录tab"):
            #使用yaml进行数据驱动
            self.steps("../base/main.yaml")
            # self.find("xpath", "//*[@text='通讯录']").click()
            return Address(self._driver)

    def goto_tab3(self):
        pass

    def goto_tab4(self):
        pass
