"""
添加成员——成员详细信息填写界面
"""
from python_appium_po.pages.base_page import BasePage


class AddInfoPage(BasePage):
    def addmember(self,key):
        #初始化sendkeys的key值
        self._key={
            "name":key["name"],
            "account":key["account"],
            "phone":key["phone"],
            "email":key["email"]
        }
        self.steps('../datas/addinfopage.yaml')

