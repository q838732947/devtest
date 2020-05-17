from app.base.BasePage import Basepage


class chatWindow(Basepage):
    def sendmsg(self,msg):
        # 输入聊天内容
        self.find("id", "com.tencent.wework:id/dx1").send_keys(f"{msg}")
        # 点击发送
        self.find("id","com.tencent.wework:id/dwx").click()
