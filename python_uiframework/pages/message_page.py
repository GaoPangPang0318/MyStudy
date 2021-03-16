"""
消息（首页）
"""
from python_uiframework.pages.base_page import BasePage
from python_uiframework.pages.contacts_page import ContactsPage


class MessagePage(BasePage):

    def go_to_contact(self):
        self.steps("../datas/messagepage.yaml", "go_to_contact")
        return ContactsPage(self.driver)
