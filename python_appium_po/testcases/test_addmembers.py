import yaml

from python_appium_po.pages.app import App


class TestAddmembers:
    def setup(self):
        self.app = App()

    def test_addmembers(self):
        with open("../datas/testdatas.yaml", "r", encoding="utf-8") as f:
            key = yaml.safe_load(f)
        #获取addmember返回的toast并进行断言
        toast = self.app.goto_main().go_to_contact().go_to_addmembers().go_to_addinfo().addmember(key)
        assert "添加成功" == toast
