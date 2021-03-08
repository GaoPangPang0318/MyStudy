"""
添加成员——成员详细信息填写界面
"""
from python_appium_po.pages.base_page import BasePage


class AddInfoPage(BasePage):
    def addmember(self):
        self.steps('../datas/addinfopage.yaml')
