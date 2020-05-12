import pytest


class TestPytest:
    def setup(self):
        print("setup")
        pass

    def teardown(self):
        print("teardown")
        pass

    # @pytest.fixture(scope="function")
    # def fixture(self):
    #     print("before fixture")
    #     yield
    #     print("end fixture")

    @pytest.mark.skip("test skip mark")
    def test_case1(self):
        print("case1")
        pass

    @pytest.mark.p1
    def test_case2(self):
        print("case2")
        # assert 1 == 2
        pass

    @pytest.mark.parametrize("a,b,c", [(1, 2, 3), (4, 5, 6)])
    def test_case3(self, a, b, c):
        print(f"case3,a={a},b={b},c={c}")


if __name__ == '__main__':
    # pytest.main(["-m", "p1"])
    pytest.main(["-m", "p1"])
    # pytest.main()

