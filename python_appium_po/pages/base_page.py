"""
基类
"""
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # 定义find函数，用于定位元素，并返回找到的元素

    def find(self,locator:dict):
        """
        查找元素
        :param locator:Dict (by,locator)=(BY.XPath,XXX)
        :return:
        """
        return self.driver.find_element(*locator)

    def find_click(self,locator:dict):
        """
        查找元素并点击
        :param locator:locator:Dict (by,locator)=(BY.XPath,XXX)
        :return:
        """
        self.find(locator).click()

    def find_senkeys(self,locator:dict,key):
        """
        查找元素并传值
        :param locator:locator:Dict (by,locator)=(BY.XPath,XXX)
        :param key:传送值
        :return:
        """
        self.find(locator).send_keys(key)

    def steps(self, path):
        """
        数据加载，步骤和测试数据如何一起加载？
        :param path:
        :return:
        """
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if step["action"]=="find_click":
                self.find_click(step["locator"])
            #测试数据如何传递？？想要单独用一个文件
            elif step["action"]=="find_sendkeys":
                self.find_senkeys(step["locator"],step["value"])