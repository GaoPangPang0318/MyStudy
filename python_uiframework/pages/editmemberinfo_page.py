"""
编辑成员信息界面：
    成员个人信息编辑
    删除成员
"""
from python_uiframework.pages.base_page import BasePage


class Editmemberinfo(BasePage):
    def deletemember(self):
        self.steps('../datas/editmemberinfopage.yaml', 'deletemember')
