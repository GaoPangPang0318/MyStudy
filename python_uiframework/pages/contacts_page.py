"""
通讯录界面
"""
from python_uiframework.pages.base_page import BasePage
from python_uiframework.pages.memberinfo_page import MemberInfo


class ContactsPage(BasePage):
    def go_to_memberinfo(self,name):
        # 又一个变量，删除成员名字 没加上
        self._params['delname']=name
        self.steps("../datas/contactspage.yaml", "go_to_memberinfo")
        return MemberInfo(self.driver)
