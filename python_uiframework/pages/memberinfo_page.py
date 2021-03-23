"""
个人信息：
    邀请加入
    发送信息
    语音信息
    编辑特殊标记
"""
from python_uiframework.pages.base_page import BasePage
from python_uiframework.pages.specialinfo_page import SpecialInfo


class MemberInfo(BasePage):
    def go_to_memberinfospecial(self):
        self.steps('../datas/memberinfopage.yaml', 'go_to_memberinfospecial')
        return SpecialInfo(self.driver)
