from app.base.BasePage import Basepage
import allure


class chatWindow(Basepage):
    def sendmsg(self, msg):
        # 输入聊天内容
        with allure.step(f"输入聊天内容：{msg}"):
            self.find("id", "com.tencent.wework:id/dx1").send_keys(f"{msg}")
        # 点击发送
        with allure.step("点击发送"):
            self.find("id", "com.tencent.wework:id/dwx").click()
