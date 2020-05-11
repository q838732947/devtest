from web.page.elements import TestFindElement


class LoginPage(TestFindElement):
    username_element = '//[@id="login_field"]'
    password_element = '//[@id="password"]'
    button_element = '//input[@name="commit"]'
    img_element = '//*[@id="user-links"]/li[3]/details/summary/img'

    def send_username(self, selenium, number):
        return self.find_xpath_send(selenium, self.username_element,number)

    def send_password(self, selenium, number):
        return self.find_xpath_send(selenium, self.password_element,number)

    def click_button(self, selenium):
        return self.find_xpath_click(selenium,self.button_element)

    def click_img(self, selenium):
        return self.find_xpath_click(selenium,self.img_element)