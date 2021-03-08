"""
消息页面
"""
from python_appium_po.pages.base_page import BasePage
from python_appium_po.pages.contacts_page import ContactsPage

class MessagePage(BasePage):
    def go_to_contact(self):
        self.steps("../datas/messagepage.yaml")
        return ContactsPage(self.driver)