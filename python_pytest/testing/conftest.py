"""
作业要求：
    1.创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
    2.将 fixture 方法存放在 conftest.py ，设置 scope=module
"""
import pytest

from python_pytest.calculator.calculator import Calculator


@pytest.fixture(scope="module")
def get_calc():
    """
        获取计算器实例
    :return: 计算机实例
    """
    print("获取计算器实例")
    calc=Calculator()
    return calc





