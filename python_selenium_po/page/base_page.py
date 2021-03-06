"""
父类
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    base_url=""

    def __init__(self,driver:WebDriver=None):
        if driver == None:
            # 复用浏览器，需要设置 option.debugger_address
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # 创建完driver ， 立刻设置隐式等待
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    def quit_driver(self):
        """
        退出driver
        :return:
        """
        self.driver.quit()

    def find_click(self,loactor,value):
        """
        定位元素并点击
        :param loactor: 定位方法
        :param value: 定位值
        """
        self.driver.find_element(loactor,value).click()

    def find_sendkeys(self,loactor,value,key):
        """
        定位元素并传值
        :param loactor: 定位方法
        :param value: 定位值
        :param key: sendkeys的值
        """
        self.driver.find_element(loactor, value).send_keys(key)


