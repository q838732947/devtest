import json

import pytest


class TestJson:
    def test_jsondumps(self):  # json.dumps用于将python对象编码成json字符串
        data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4}]
        j = json.dumps(data)
        print(type(j))
        print(j)
        a = [1, 2, 3, 4, 5]
        print(a[:])  # 12345
        print(a[0:])
        print(a[:100])
        print(a[-1:-5:-1])


if __name__ == '__main__':
    pytest.main()
