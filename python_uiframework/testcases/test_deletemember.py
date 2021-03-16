from time import sleep

import yaml

from python_uiframework.pages.app import App


class TestDeleteMenber:
    def setup(self):
        self.app = App()

    def test_deletemembers(self):
        self.app.goto_main().go_to_contact().go_to_memberinfo('测试005').go_to_memberinfospecial().go_to_editmemberinfo().deletemember()
