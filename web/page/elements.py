from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestFindElement(object):

    def find_css_send(self, selenium, css, number):
        try:
            WebDriverWait(selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
            selenium.find_element_by_css_selector(css).send_keys(number)
        except:
            print("%s元素不可见" % css)

    def find_id_send(self, selenium, id, number):
        try:
            WebDriverWait(self, selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.ID, id)))
            selenium.find_element_by_id(id).send_keys(number)
        except:
            print("%s元素不可见" % id)

    def find_name_send(self, selenium, name, number):
        try:
            WebDriverWait(selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.NAME, name)))
            selenium.find_element_by_name(name).send_keys(number)
        except:
            print("%s元素不可见" % name)

    def find_xpath_send(self, selenium, xpath, number):
        try:
            WebDriverWait(selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
            selenium.find_element_by_xpath(xpath).send_keys(number)
        except:
            print("%s元素不可见" % xpath)

    # click点击方法封装
    def find_css_click(self, selenium, css):
        try:
            WebDriverWait(selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
            selenium.find_element_by_css_selector(css).click()
        except:
            print("%s元素不可见" % css)

    def find_id_click(self, selenium, id):
        try:
            WebDriverWait(selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.ID, id)))
            selenium.find_element_by_id(id).click()
        except:
            print("%s元素不可见" % id)

    def find_name_click(self, selenium, name):
        try:
            WebDriverWait(selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.NAME, name)))
            selenium.find_element_by_name(name).click()
        except:
            print("%s元素不可见" % name)

    def find_xpath_click(self, selenium, xpath):
        try:
            WebDriverWait(selenium, 10, 0.5).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
            selenium.find_element_by_xpath(xpath).click()
        except:
            print("%s元素不可见" % xpath)

    def find_xpath(self, selenium, xpath):
        return selenium.find_element_by_xpath(xpath)
