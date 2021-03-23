"""
成员个人信息界面：
    推介给联系人
    设为星标联系人
    消息特别提醒
    添加到手机通讯录
"""
from python_uiframework.pages.base_page import BasePage
from python_uiframework.pages.editmemberinfo_page import Editmemberinfo


class SpecialInfo(BasePage):
    def go_to_editmemberinfo(self):
        self.steps('../datas/specialinfopage.yaml', 'go_to_editmemberinfo')
        return Editmemberinfo(self.driver)
