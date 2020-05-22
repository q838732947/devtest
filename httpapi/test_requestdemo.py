import pytest
import requests


class TestA:
    def test_a(self):
        url = "http://httpbin.testing-studio.com/get"
        params = {}
        data = {}
        headers = {}
        r = requests.get(url=url, params=params, headers=headers)
        print(r.text)
        # r2 = requests.post(url=url, data=data, headers=headers)
        # print(r2.text)


if __name__ == "__main__":
    pytest.main(['-s', 'test_requestdemo.py'])
