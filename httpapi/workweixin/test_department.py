import json
import time
import allure
import pytest
import requests
import yaml

# todo:调用httpBase重写
def get_token() -> str:
    with open("./department.yaml") as f:
        d = yaml.safe_load(f)
        id, secret, access_token, last_time = d['id'], d['secret'], d['access_token'], d['last_time']
    now = int(time.time())
    # print(d)
    if now - last_time > 7200:
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}'
        r = requests.get(url=url)
        print(r.json())
        d['access_token'] = r.json()['access_token']
        d['last_time'] = now
        # print(d)
        with open("./department.yaml", "w") as f:
            yaml.dump(d, f)
        return d['access_token']
    else:
        return access_token


def yaml_steps(path):
    with allure.step("获取token"):
        access_token = get_token()
    with open(path) as f:
        request = yaml.safe_load(f)
        # print(request)
        for r in request:
            print(r["comment"])
            with allure.step(r["comment"]) :
                params = {"access_token": access_token}
                data = {}
                if r['params'] is not None:
                    for key in r['params'].keys():
                        params[key] = r['params'][key]
                if r['data'] is not None:
                    data = r['data']
                re = requests.request(method=r["method"], url=r["url"], params=params, json=data)
                # if r["method"] == "get":
                #     re = requests.get(url=url, params=params, json=data)
                # if r["method"] == "post":
                #     re = requests.post(url=url, params=params, json=data)
                print(re.json())
                if r['assert'] is not None:
                    for key in r['assert'].keys():
                        assert r['assert'][key] == re.json()[key]


class Test_department:
    def setup(self):
        self.access_token = get_token()

    @pytest.mark.skip
    def test_get_department(self, id=None):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}'
        if id is not None:
            url = url + f"id={id}"
        r = requests.get(url=url)
        print(r.json())
        assert r.json()["errcode"] == 0

    @pytest.mark.skip
    @pytest.mark.parametrize("name,parentid", [("技术部", 1), ("行政中心", 1)])
    def test_create_department(self, name, parentid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}"
        data = {
            "name": name,
            "parentid": parentid,
        }
        r = requests.post(url=url, data=json.dumps(data))
        print(r.json())
        assert r.json()["errcode"] == 0

    @pytest.mark.skip
    @pytest.mark.parametrize("id,name,name_en", [(2, "技术研发中心", None), (3, "财务部", "caiwu")])
    def test_update_department(self, id, name, name_en):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}'
        data = {"id": id}
        if name is not None:
            data['name'] = name
        if name_en is not None:
            data['name_en'] = name_en
        r = requests.post(url=url, json=data)
        print(r.json())
        assert r.json()["errcode"] == 0

    @pytest.mark.skip
    @pytest.mark.parametrize("id", [2, 3])
    def test_delete_department(self, id):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={id}'
        r = requests.get(url=url)
        print(r.json())
        assert r.json()["errcode"] == 0


class Test_Department_withyaml:
    def test_with_yaml(self):
        yaml_steps(path="./testdepartment.yaml")


if __name__ == '__main__':
    pytest.main()
