import random

import pytest

from httpapi.workweixin.POcase.api.externalcontact import externalContact


class Test_externalContact:
    def setup_class(self):
        self.tag = externalContact()

    @pytest.mark.parametrize("name", ["zhangsan2"])
    def test_add_not_exist(self, name):
        # name不存在直接添加，存在的话先删除再添加
        names = self.tag.get_allname()
        if names is not None and name in names:
            self.tag.del_corp_tag(self.tag.get_tag_id_by_name(name))
        r = self.tag.add_corp_tag(name)
        assert r["errcode"] == 0
        assert r["errmsg"] == "ok"
        assert r["tag_group"]["tag"][0]["name"] == name

    @pytest.mark.parametrize("name", ["zhangsan3"])
    def test_add_is_exist(self, name):
        # name存在直接添加，不存在的话先添加再添加
        names = self.tag.get_allname()
        if names is None or name not in names:
            self.tag.add_corp_tag(name)
        r = self.tag.add_corp_tag(name)
        assert r["errcode"] in (40068, 40071)

    def test_get(self):
        assert self.tag.get_corp_tag_list()["errcode"] == 0

    def test_edit(self):
        old_name = "zhangsan3"
        new_name = "lisi"
        names = self.tag.get_allname()
        if old_name not in names:
            self.tag.add_corp_tag(old_name)
        if new_name not in names:
            new_name = "lisi" + str(random.randint(1, 1000))
        tag_id = self.tag.get_tag_id_by_name(old_name)
        assert self.tag.edit_corp_tag(tag_id, new_name)["errcode"] == 0
        names = self.tag.get_allname()
        assert new_name in names

    def test_del(self):
        names = self.tag.get_allname()
        if names is None:
            self.tag.add_corp_tag("lisi")
            names = self.tag.get_allname()
        for name in names:
            self.tag.del_corp_tag(self.tag.get_tag_id_by_name(name))
        assert self.tag.get_allname() is None

    def test_with_yaml(self):
        self.tag.yaml_steps(path="test_externalContact.yaml", module=self.tag.module)
