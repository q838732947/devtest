import time

import allure
import requests
import yaml


def get_token(module) -> str:
    with open("./baseconfig.yaml") as f:
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
        with open("./baseconfig.yaml", "w") as f:
            yaml.dump(x, f)
        return d['access_token']
    else:
        return access_token

def yaml_steps(path):
    with allure.step("获取token"):
        access_token = get_token("address")
    with open(path) as f:
        request = yaml.safe_load(f)
        # print(request)
        for r in request:
            print(r["comment"])
            with allure.step(r["comment"]):
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


if __name__ == '__main__':
    yaml_steps("./testdepartment.yaml")
