"""
基类
"""
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # 定义find函数，用于定位元素，并返回找到的元素

    def find(self,by,locator):
        """
        查找元素
        """
        return self.driver.find_element(by,locator)

    def find_click(self,by,locator):
        """
        查找元素并点击

        """
        self.find(by,locator).click()

    def find_sendkeys(self,by,locator,key):
        """
        查找元素并传值
        """
        self.find(by,locator).send_keys(key)

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
                self.find_click(step["by"],step["locator"])
            #测试数据如何传递？？想要单独用一个文件
            elif step["action"]=="find_sendkeys":
                self.find_sendkeys(step["by"],step["locator"],step["value"])