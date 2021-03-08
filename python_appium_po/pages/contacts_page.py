"""
通讯录界面
"""
from python_appium_po.pages.addmembers_page import AddMembersPage
from python_appium_po.pages.base_page import BasePage


class ContactsPage(BasePage):

    def go_to_addmembers(self):
        self.steps("../datas/contactspage.yaml")
        return AddMembersPage(self.driver)
