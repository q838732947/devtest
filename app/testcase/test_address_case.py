from app.base.app import App
import pytest


class TestAddressCase:

    @pytest.mark.parametrize("name,gender,phone", [
        # ("测试name12", "男", "18600000012"),
        ("测试name15", "女", "18600000015"),

    ])
    def test_addmember(self, name, gender, phone):
        App().start().main().goto_tab2().addmember().manual_invite().addname(f"{name}").selectgender(
            f"{gender}").addphone(
            f"{phone}").save().back()

    def test_delmember(self, name="测试"):
        App().start().main().goto_tab2().search().searchtext(
            f"{name}").pointfirstresult().moreinfo().editmember().delMember().back()

    @pytest.mark.parametrize("name,msg", [
        ("陈灵", "hello"),
        # ("灵芝","words")
    ])
    def test_say(self, name, msg):
        App().start().main().goto_tab2().search().searchtext(f"{name}").pointfirstresult().sendmessage().sendmsg(
            f"{msg}")
