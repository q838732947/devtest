import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:
    _black_list = [("id", "com.tencent.wework:id/b_4")]
    _error_count = 0
    _error_max = 10
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=None):
        try:
            # WebDriverWait(self._driver, 10).until(
            #     expected_conditions.invisibility_of_element_located((by, locator)))
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                             locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        # {value}
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("%s" % param, self._params[param])
                            element.send_keys(content)

    def findtoast(self, toasttext=""):
        self._driver.find_element(MobileBy.XPATH, f"//*[@class='android.widget.Toast' and @text='{toasttext}']")

    def rollfind_bytext(self, text):
        ele = self.find(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')
        return ele