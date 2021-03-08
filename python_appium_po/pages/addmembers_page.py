"""
添加成员界面
"""
from python_appium_po.pages.addinfo_page import AddInfoPage
from python_appium_po.pages.base_page import BasePage


class AddMembersPage(BasePage):
    def go_to_addinfo(self):
        self.steps("../datas/addmemberspage.yaml")
        return AddInfoPage(self.driver)
