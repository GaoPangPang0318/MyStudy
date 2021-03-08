from python_appium_po.pages.app import App


class TestAddmembers:
    def setup(self):
        self.app=App()

    def test_addmembers(self):
        self.app.goto_main().go_to_contact().go_to_addmembers().go_to_addinfo().addmember()

