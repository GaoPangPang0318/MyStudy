"""
基类
"""
import json
from typing import List, Dict
import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from python_uiframework.conftest import root_log


class BasePage:
    #存放替换的值
    _params = {}
    #黑名单
    _blacklist=[(MobileBy.ID,'com.tencent.wework:id/ig0')]
    #最大错误次数
    _max_num=10
    # 错误次数
    _error_num = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def setup_implicitly_wait(self, timeout):
        """
        隐式等待方法
        :param timeout: 等待时间
        :return: None
        """
        self.driver.implicitly_wait(timeout)

    def find(self, by, locator):
        """
        查找元素
        :param by: 定位方法
        :param locator: 定位值
        :return: element
        """
        #日志输出
        root_log.info(f"start find: by={by} , locator = {locator}")
        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            self.setup_implicitly_wait(10)

            #日志输出
            root_log.info(f" Success！find: by={by} , locator = {locator}")

            return element
        except Exception as e:
            #日志输出
            root_log.info(f"Can not find the element。")

            # 处理黑名单逻辑
            self.setup_implicitly_wait(2)

            # 报错截图
            self.driver.get_screenshot_as_file("Error.png")
            allure.attach.file("Error.png", attachment_type=allure.attachment_type.PNG)

            # 查找错误次数超上限，报错，不继续进行查找
            if self._error_num > self._max_num:
                self._error_num = 0
                self.setup_implicitly_wait(10)
                raise e
            # 每次进except 一次都执行+1操作
            self._error_num += 1
            # 处理黑名单
            for ele in self._blacklist:
                #日志输出
                root_log.info(f" Deal with blackList:{ele}")

                # find_elements 会返回元素的列表[ele1,ele2.....]，如果没有元素会返回一个空列表，find_element没查到会报错，影响程序进一步运行
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()

                    # 日志输出
                    root_log.info(f" Success! blackList:{ele}")

                    return self.find(by, locator)
            # 如果黑名单都处理完，仍然没有找到想要的元素，则抛出异常
            raise e

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

    def swip_click(self, text):
        """
        滑动查找元素,并进行黑名单操作
        :param text: 变量，用户定义查找元素名
        :return: None
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def steps(self, path, func_name):
        """
        步骤数据加载
        :param path:yaml文件路径
        """
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[func_name]

        #值替换操作
        raw = json.dumps(steps)
        for key, value in self._params.items():
            #注意特殊格式替换方法
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)

        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "find_sendkeys":
                self.find_sendkeys(step["by"], step["locator"],step["value"])

