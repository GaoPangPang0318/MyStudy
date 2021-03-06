"""
添加成员页PO
"""


from selenium.webdriver.common.by import By

from python_selenium_po.page.base_page import BasePage


class AddMembersPage(BasePage):

    def add_members(self,username,englishname,account,phonenum,telnum,email,address,title):
        """
        添加成员详细信息
        :return:
        """

        #姓名
        self.find_sendkeys(By.ID,"username",username)
        #别名
        self.find_sendkeys(By.ID,"memberAdd_english_name",englishname)
        #账号
        self.find_sendkeys(By.ID,"memberAdd_acctid",account)
        #性别
        #二选一：男 或 女

        #手机
        self.find_sendkeys(By.ID,"memberAdd_phone",phonenum)
        #座机
        self.find_sendkeys(By.ID,"memberAdd_telephone",telnum)
        #邮箱
        self.find_sendkeys(By.ID,"memberAdd_mail",email)
        #地址
        self.find_sendkeys(By.ID,"memberEdit_address",address)
        #职务
        self.find_sendkeys(By.ID,"memberAdd_title",title)
        #身份
        #二选一：普通成员 或 上级

        #对外信息——职务
        #二选一:同步公司内职务 或 自定义

        #通过右键或短信发送企业邀请
        #二选一：选中 或 不选中

        #保存
        self.find_click(By.CSS_SELECTOR,".js_btn_save")

        return True





