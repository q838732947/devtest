import allure
import pytest


# Allure官方文档https://docs.qameta.io/allure/2.0/)
# 在测试执行期间收集结果 pytest [测试文件] -s -q --alluredir=./result/
# pytest --alluredir=/tmp/my_allure_results
#
# 查看测试报告，方案1：在线查看报告，直接打开默认浏览器展示当前报告
# allure serve /tmp/my_allure_results
#
# 方案2：从结果生成报告，这是启动一个tomcat的服务，分两步：生成报告、打开报告
# allure generate ./result/ -o ./report/ --clean (覆盖路径加--clean)
# allure open -h 127.0.0.1 -p 8883 ./report
@allure.feature("allure模块")
class Test_Allure:
    @allure.story("成功")
    def test_success(self):
        """this test succeeds"""
        with allure.step("步骤1"):pass
        with allure.step("步骤2"): pass
        assert True

    @allure.story("失败")
    def test_failure(self):
        """this test fails"""
        assert False

    def test_skip(self):
        """this test is skipped"""
        pytest.skip('for a reason!')

    def test_broken(self):
        raise Exception('oops')

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_xfail_expected_failure(self):
        """this test is an xfail that will be marked as expected failure"""
        assert False

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_xfail_unexpected_pass(self):
        """this test is an xfail that will be marked as unexpected success"""
        assert True

    @pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
    def test_skip_by_triggered_condition(self):
        pass


if __name__ == '__main__':
    pytest.main(['test_allure.py', '-s', '--alluredir=/tmp/my_allure_results'])
