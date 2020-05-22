import json
import re
from jsonpath import jsonpath
from httpapi.workweixin.POcase.api.BaseApi import BaseApi


class externalContact(BaseApi):
    module = "externalcontact"

    def __init__(self):
        self.token = self.get_token(module=self.module)

    def add_corp_tag(self, tag_name):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": "test",
                "tag": [{"name": tag_name}]
            }
        }
        return self.send_api(data)

    def get_corp_tag_list(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": []
            }
        }
        return self.send_api(data)

    def del_corp_tag(self, tag_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [
                    tag_id
                ]
            }
        }
        return self.send_api(data)

    def edit_corp_tag(self, tag_id, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": tag_id,
                "name": name
            }
        }
        return self.send_api(data)

    def get_tag_id_by_name(self, name=""):
        # if name == "":
        #     tag_id = jsonpath(self.get_corp_tag_list(), '$..tag[0].id')
        # else:
        l = self.get_corp_tag_list()
        tag_id = jsonpath(l, f'$..tag[?(@.name=="{name}")].id')
        if tag_id is False:
            raise Exception("name not is exist")
        return tag_id[0]

    def get_allname(self) -> list:
        r = self.get_corp_tag_list()
        if not r["tag_group"]:
            return None
        else:
            pattern = re.compile('"name": "(.+?)"')  # 设定正则模式
            result = pattern.findall(json.dumps(r))  # 获得结果
            return result


if __name__ == '__main__':
    tag = externalContact()
    print(tag.get_tag_id_by_name("zhangsan3"))
