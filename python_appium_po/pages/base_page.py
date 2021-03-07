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

    def find(self, by, locator: None):
        try:

            # find_elements 和 find_element的却别?
            # find_elements 返回匹配元素的list  ； find_element返回匹配的元素
            el = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            # 找到元素，元素查找失败变量更新为0
            self._error_count = 0
            return el  # 返回找到的element
        except Exception as e:
            # 查找元素失败，计数+1
            self._error_count = +1
            # 但失败次数超过上限，抛出异常
            if self._error_count >= self._error_max:
                print(self._error_count)
                raise e
            # 对弹出框进行操作，遍历_black_list
            for black in self._black_list:
                b_els: list = self._driver.find_elements(*black)  # 使用元祖结构的方法查找元素，并返回元素列表
                # 若存在弹出框，则进行操作
                if len(b_els) > 0:
                    b_els[0].click()
                    # 继续查找元素
                    return self.find(by, locator)
            raise e  # 你存在的含义是啥？超过10次就会抛异常，这边不需要了吧？

        # 定义send方法，用于send_keys

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
        except Exception as e:
            self._error_count = +1
            if self._error_count >= self._error_count:
                raise e
            for black in self._black_list:
                b_els = self._driver.find_elements(*black)
                if len(b_els) > 0:
                    b_els[0].click()
                    return self.send(value, by, locator)
            raise e

        # 加载数据

    def steps(self, path):  # Path：yaml文件路径
        with open(path, encoding="utf-8") as f:  # 设置encodeing为了防止数据文件出现中文导致乱码
            steps = yaml.safe_load(f)
            # 取文件数据
            for step in steps:
                # 通过by和locator 进行元素定位
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                # 通过不同的action，来进行不同的操作
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        # 记住这个写法，感觉会很有用
                        content: str = step["value"]  # content=“{value}”
                        for param in self._params:  # param为key，此处为：value
                            content = content.replace("{%s}" % param, self._params[param])  # "{%s}"%param ==“{value}”
                        self.send(content, step["by"], step["locator"])

                    # 为了搞清楚以上的操作 做的简答的操作
                    # params = {"value": "abc"}
                    # content = "{value}"
                    # print(params)
                    # print(type(params))
                    # for param in params:
                    #     print(type(param))
                    #     print(param)
                    #     print(content.replace("{%s}" % param, params[param]))
