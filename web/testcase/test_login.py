import allure

from web.page.LoginPage import LoginPage


@allure.feature('登陆功能')
class TestLogin(object):
    @allure.story('登陆')
    def test_login(self, selenium, metadata):
        login_page = LoginPage()
        result = 'zhengxingqu'
        with allure.step("点击login链接"):
            pass
            login_page.find_xpath_click(selenium, "//a[@href='/login']")
        with allure.step("输入用户名"):
            pass
            login_page.send_username(selenium, metadata['username'])
        with allure.step("输入密码"):
            pass
            login_page.send_password(selenium, metadata['password'])
        with allure.step("点击登陆按钮"):
            pass
            login_page.click_button(selenium)
        with allure.step("点击头像"):
            pass
            login_page.click_img(selenium)
        with allure.step("获取用户名"):
            pass
            name_text = login_page.find_xpath(selenium,
            '//*[@id="user-links"]/li[3]/details/details-menu/div[1]/a/strong').text
        assert name_text == result