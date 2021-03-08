import yaml

from python_appium_po.pages.app import App


class TestAddmembers:
    def setup(self):
        self.app = App()

    def test_addmembers(self):
        with open('../datas/testdatas.yaml', encoding="utf-8") as f:
            key = yaml.safe_load(f)
        self.app.goto_main().go_to_contact().go_to_addmembers().go_to_addinfo().addmember(key)
