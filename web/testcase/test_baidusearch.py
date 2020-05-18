from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest, allure


@allure.feature("搜索模块")
class Test_BaiduSearch:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @allure.story("搜索用例")
    @pytest.mark.parametrize("searchkey", ["pytest", "allure", "凌晨灵修"])
    def test_search(self, searchkey):
        with allure.step("打开百度首页"):
            self.driver.get(url="https://www.baidu.com")
        with allure.step("输入搜索词"):
            self.driver.find_element(By.ID, "kw").send_keys(f"{searchkey}")
        with allure.step("点击百度一下"):
            self.driver.find_element(By.ID, "su").click()
        with allure.step("保存当前页面截图"):
            sleep(2)
            self.driver.save_screenshot(f"./result/{searchkey}.png")
            # 在测试报告中展示截图
            allure.attach.file(f"./result/{searchkey}.png", attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    # pytest test_baidusearch.py --alluredir ./result/
    # 在线查看报告，直接打开默认浏览器展示当前报告
    # allure serve ./result/
    pytest.main()
