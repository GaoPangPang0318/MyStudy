"""
基类
"""
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    #私有变量，存放sendkeys中的值
    _key = {}

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        """
        查找元素
        :param by: 定位方法
        :param locator: 定位值
        :return: element
        """
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        """
        查找元素并点击
        :param by: 定位方法
        :param locator: 定位值
        """
        self.find(by, locator).click()

    def find_sendkeys(self, by, locator, key):
        """
        查找元素并传值
        :param by: 定位方法
        :param locator: 定位值
        """
        self.find(by, locator).send_keys(key)

    def steps(self, path):
        """
        步骤数据加载
        :param path:yaml文件路径
        """
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find_sendkeys":
                #分离测试数据，测试数据单独一个yaml文件
                content:str=step["value"]
                for key in self._key:
                    content=content.replace("{%s}"%key,self._key[key])
                self.find_sendkeys(step["by"], step["locator"], content)
