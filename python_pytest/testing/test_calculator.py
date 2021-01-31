"""
课后作业：
    1.补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
    2.创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
    3.将 fixture 方法存放在 conftest.py ，设置 scope=module
    4.控制测试用例顺序按照【加-减-乘-除】这个顺序执行
    5.结合 allure 生成本地测试报告
"""

import pytest
import yaml


def get_data(dataflag:str)->list:
    """
        获取yaml中的数据
    :param dataflag: 获取测试数据类型标志  add：加法测试数据 sub:减法测试数据 mul：乘法测试数据 div：除法测试数据
    :return:  测试数据和标记的list
    """
    with open("../datas/cal_datas.yml") as f:
        data=yaml.safe_load(f)[dataflag]
        testing_data=data['datas']  #测试数据
        ids=data['ids']  #ids
        return [testing_data,ids]




class TestCal:
    #加法测试用例，并进行参数化
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",get_data("add")[0],ids=get_data("add")[1])
    def test_add(self,a,b, expect,get_calc):
        result=get_calc.add(a,b)
        if isinstance(result,float):
             result=round(result,2)
        assert result==expect

    #除法测试用例
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", get_data("div")[0], ids=get_data("div")[1])
    def test_div(self,a,b, expect,get_calc):
        result = get_calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect


    #减法测试用例
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_data("sub")[0], ids=get_data("sub")[1])
    def test_sub(self,a,b, expect,get_calc):
        result = get_calc.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    #乘法测试用例
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_data("mul")[0], ids=get_data("mul")[1])
    def test_mul(self,a,b, expect,get_calc):
        result = get_calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

