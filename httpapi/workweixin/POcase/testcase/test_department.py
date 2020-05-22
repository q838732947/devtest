from httpapi.workweixin.POcase.api.BaseApi import BaseApi


class Test_Department_withyaml:
    module = "address"

    def setup(self):
        self.c = BaseApi()

    def test_with_yaml(self):
        self.c.yaml_steps(path="./testdepartment.yaml", module='address')
