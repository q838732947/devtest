import pytest


@pytest.fixture()
def f1():
    print("###" * 20 + "打印f1")  # 默认不会自动加载


@pytest.fixture(scope='function', autouse=True)  # scope默认为function，autouse设为True后，会默认加载该函数，但是无法用于传参
def f2():
    print("###" * 20 + "打印f2")


@pytest.fixture()
def f3():
    a, b, c = 1, 2, 3
    print("###" * 20 + "打印f3")
    return (a, b, c)  # fixture函数可以用于传参


@pytest.fixture()
def f4():
    print("00000000000")
    yield  # yeild 会在调用fixture方法前后分别执行yield前后的代码
    print("1111111111")


@pytest.fixture(scope='class', autouse=True)
def f5():
    print("BeginClass")
    yield
    print("EndClass")


def test_outerclass():
    print("outterclass")


class TestFixture:

    def test1(self):
        print("test1")

    @pytest.mark.usefixtures("f1")  # 指定使用f1,这样使用无法传参
    def test2(self):
        print("test2")

    def test3(self, f3):
        a, b, c = f3[0], f3[1], f3[2]
        print(f"test3,a={a},b={b},c={c}")

    def test4(self, f4):
        print("test4")


if __name__ == '__main__':
    pytest.main('-s test_fixture.py')
