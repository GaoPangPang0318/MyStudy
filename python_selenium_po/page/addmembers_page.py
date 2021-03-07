"""
添加成员页PO
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from python_selenium_po.page.base_page import BasePage

class AddMembersPage(BasePage):

    def add_members(self, username, englishname, account, gender, phonenum, telnum, email, address, title, identity):
        """
        添加成员详细信息
        :return:
        """
        # 姓名
        self.find_sendkeys(By.ID, "username", username)
        # 别名
        self.find_sendkeys(By.ID, "memberAdd_english_name", englishname)
        # 账号
        self.find_sendkeys(By.ID, "memberAdd_acctid", account)
        # 性别_二选一：男 或 女
        if gender == "男":
            self.find_click(By.XPATH, "//*[@name='gender' and @value='1']")
        elif gender == "女":
            self.find_click(By.XPATH, "//*[@name='gender' and @value='2']")
        # 手机
        self.find_sendkeys(By.ID, "memberAdd_phone", phonenum)
        # 座机
        self.find_sendkeys(By.ID, "memberAdd_telephone", telnum)
        # 邮箱
        self.find_sendkeys(By.ID, "memberAdd_mail", email)
        # 地址
        self.find_sendkeys(By.ID, "memberEdit_address", address)
        # 职务
        self.find_sendkeys(By.ID, "memberAdd_title", title)
        # 身份 二选一：普通成员 或 上级  identity_stat
        if identity == "普通成员":
            self.find_click(By.XPATH, "//*[@name='identity_stat' and @value='0']")
        elif identity == "上级":
            self.find_click(By.XPATH, "//*[@name='identity_stat' and @value='1']")

        # 对外信息——职务二选一:同步公司内职务 或 自定义
        # if position=="同步公司内职务":
        #     self.find_click(By.XPATH,"//*[@name='extern_position_set' and @value='sync']")
        # else:
        #     self.find_click(By.XPATH,"//*[@name='extern_position_set' and @value='custom']")
        # 怎么处理还没想好
        # self.find_sendkeys(By.XPATH,"//*[@name='extern_position']",position)
        # 通过邮件或短信发送企业邀请
        # 怎么处理没想好

        # 保存
        self.find_click(By.CSS_SELECTOR, ".js_btn_save")
        return True

    def get_members(self):
        '''
        获取所有的联系人姓名
        :return:
        '''
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")))
        eles_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))
        return names
