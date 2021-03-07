"""
企业微信首页PO
"""
from selenium.webdriver.common.by import By
from python_selenium_po.page.addmembers_page import AddMembersPage
from python_selenium_po.page.base_page import BasePage


class IndexPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_addmembers(self):
        """
        添加成员
        :return:
        """
        self.find_click(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
        return AddMembersPage(self.driver)
