"""
课后作业
    1.补全计算器中加法和除法的测试用例
    2.使用参数化完成测试用例的自动生成
    3.在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：
    使用等价类，边界值，因果图等设计测试用例
    测试用例中添加断言，验证结果
    灵活使用 setup(), teardown() , setup_class(), teardown_class()

"""
import pytest
from python_pytest_adv.testing.base import Base


class TestCalc(Base):
    #加法测试
    @pytest.mark.parametrize("a,b,expect",Base.get_datas("add")["datas"],ids=Base.get_datas("add")["ids"])
    def test_add(self,a,b,expect):
        result=self.calc.add(a,b)
        #
        if isinstance(result, float):
            result = round(result, 2)
        assert  result==expect

    #减法测试
    @pytest.mark.parametrize("a,b,expect", Base.get_datas("sub")["datas"], ids=Base.get_datas("sub")["ids"])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    #乘法测试
    @pytest.mark.parametrize("a,b,expect", Base.get_datas("mul")["datas"], ids=Base.get_datas("mul")["ids"])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    #除法测试
    @pytest.mark.parametrize("a,b,expect", Base.get_datas("div")["datas"], ids=Base.get_datas("div")["ids"])
    def test_div(self,a,b,expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
