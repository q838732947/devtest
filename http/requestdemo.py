import requests

if __name__ == "__main__":
    url = "http://www.baidu.com"
    params = {}
    data = {}
    headers = {}
    r = requests.get(url=url, params=params, headers=headers)
    print(r.text)
    # r2 = requests.post(url=url, data=data, headers=headers)
    # print(r2.text)
