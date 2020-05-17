from appium.webdriver.common.mobileby import MobileBy

from app.base.BasePage import Basepage


class manmulAddMember(Basepage):
    def addname(self, name):
        self.find("xpath", '//*[contains(@text,"姓名")]/..//*[@resource-id="com.tencent.wework:id/au0"]').send_keys(
            f"{name}")
        return self

    def selectgender(self, gender):
        self.find(MobileBy.ID, "com.tencent.wework:id/av2").click()
        self.find(MobileBy.XPATH,
                                 f'//*[@resource-id="com.tencent.wework:id/dqn"and @text="{gender}"]').click()
        return self

    def addphone(self, phone):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/eq7"]').send_keys(
            f"{phone}")
        return self

    def save(self):
        from app.base.addmember import addMember
        #
        # # 点击保存
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gur"]').click()
        # # toast提示添加成功
        # self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        self.steps("../base/save.yaml")
        self.findtoast("添加成功")
        return addMember(self._driver)
