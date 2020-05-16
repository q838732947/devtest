import time

import pytest


def test_single():
    print("begin")
    add3 = lambda x: x + 3
    print(add3(3))
    print("+++++" * 3)
    print(lambda x: x + 3)


def test_mulparames():
    add = lambda a, b: a * b
    print(add(3, 4))


def test_filter():
    x = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(x))


def test_replace_f():
    time.sleep = lambda x: None
    time.sleep(10000)  # 重置sleep方法，并不会等待10000s


if __name__ == '__main__':
    pytest.main()
