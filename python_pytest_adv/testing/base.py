"""
  测试基础类：
  用于对测试用例的初始化测试
"""
import yaml
from python_pytest.calculator.calculator import Calculator

class Base:
    def setup_class(self):
        #实例化计算机类
        self.calc=Calculator()
        print("开始测试")

    def teardown_class(self):
        print("结束测试")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @classmethod
    def get_datas(cls,dataflag):
        """
        定义一个获取测试数据和自定义id的类方法
        :param dataflag: yaml文件中测试数据标记 add：加法测试数据  sub：减法测试数据  mul：乘法测试数据  div：除法测试数据
        :return: 返回字典，key="datas"----测试数据  ，key="ids"---自定义id
        """
        with open("../datas/cal_datas.yml") as f:
            datas=yaml.safe_load(f)[dataflag]
            testdata=datas["datas"]
            myid=datas["ids"]
            return {"datas":testdata,"ids":myid}
