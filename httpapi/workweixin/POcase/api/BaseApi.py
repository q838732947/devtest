import json
import time
from string import Template

import allure
import requests
import yaml


class BaseApi:
    def yaml_steps(self, path, module):
        with allure.step("获取token"):
            access_token = self.get_token(module)
        with open(path) as f:
            request = yaml.safe_load(f)
            # print(request)
            for r in request:
                print(r["comment"])
                with allure.step(r["comment"]):
                    try:
                        params = {"access_token": access_token}
                        data = {}
                        if r['params'] is not None:
                            for key in r['params'].keys():
                                params[key] = r['params'][key]
                        if r['data'] is not None:
                            data = r['data']
                            if "use_var" in r.keys():
                                data = Template(json.dumps(data)).safe_substitute(save_var)
                                # print("****" * 5)
                                data = json.loads(data)
                                # print(data)

                                # for var in save_var:
                                #     data = json.dumps(data)
                                #     data = data.replace(var, save_var[var])
                                #     data = json.loads(data)
                                #     print("****"*5+"data:")
                                #     print(data)

                        re = requests.request(method=r["method"], url=r["url"], params=params, json=data)
                        # if r["method"] == "get":
                        #     re = requests.get(url=url, params=params, json=data)
                        # if r["method"] == "post":
                        #     re = requests.post(url=url, params=params, json=data)

                        if "save_var" in r.keys():
                            save_var = r["save_var"]
                            for key in save_var.keys():
                                if key == "tagid":
                                    save_var[key] = re.json()["tag_group"][0]["tag"][save_var[key]]["id"]
                        print(re.json())
                        if r['assert'] is not None:
                            for key in r['assert'].keys():
                                assert r['assert'][key] == re.json()[key]
                    except Exception:
                        print("failed")
                        continue

    def get_token(self, module) -> str:
        with open("../api/baseconfig.yaml") as f:
            x = yaml.safe_load(f)
            y = 0  # y记录当前列表指针
            for d in x:
                if d['module'] == module:
                    id, secret, access_token, last_time = d['id'], d['secret'], d['access_token'], d['last_time']
                    break
                else:
                    y += 1
        now = int(time.time())
        # print(d)
        if now - last_time > 7200:
            url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}'
            r = requests.get(url=url)
            print(r.json())
            d['access_token'] = r.json()['access_token']
            d['last_time'] = now
            x[y] = d
            with open("../api/baseconfig.yaml", "w") as f:
                yaml.dump(x, f)
            return d['access_token']
        else:
            return access_token

    def send_api(self, req: dict):
        r = requests.request(**req).json()
        print(json.dumps(r, indent=2))
        return r


if __name__ == '__main__':
    BaseApi().get_token("externalcontact")
