import json

import requests
import time


class Base:

    def get_access_token(self):
        """
        ID:企业ID
        SECRET:应用的凭证密钥
        :return:
        """
        ID = 'ww6cb5b7542d579ade'
        SECRET = 'pLdsLe2NUcNmkunLGYssPTOv6onB68UqMUamfBvFnOE'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'
        r = requests.get(url=url)
        print(r.text)
        return r.json()['access_token']

    def get_daka_data(self):
        ACCESS_TOKEN = self.get_access_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata?access_token={ACCESS_TOKEN}"
        data = {
            "opencheckindatatype": 3,
            "starttime": 1588302406,
            "endtime": 1589771164,
            "useridlist": ["ChenLing", "Lc0001"]
        }
        r = requests.post(url=url, data=json.dumps(data))
        print(r.text)

if __name__ == '__main__':
    # Base().get_access_token()
    # print(int(time.time()))
    Base().get_daka_data()
    {"errcode": 0, "errmsg": "ok",
     "access_token": "h_VfIwPRJCXd_sgWYt-LDhhtC3JRVmnoop5gEZ2jgoHukOQH58A7YAg-l4O-6W3Yy0U2TakqB2eOXfHf7k0Ud53pqzROUcLHH8kupU1ieOsDUGCNMNThEzEgCORc1SXao0hMcUWLZRpQfUhef6Y4_P-kQ5Y7_fbc8ovmlRntCS9IEsut7250RHrOAC0nDnnHwGA1pWZHkuNXMpEWm9dJ6A",
     "expires_in": 7200}
