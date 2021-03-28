# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File Name    : testcasebase
# @Time         : 2021/3/28 19:47
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import yaml


class TestCaseBase:

    @classmethod
    def get_testdata(cls, testflag):
        """
        获取测试数据
        :param test_flag: 测试数据标记
        :return: 测试数据集合
        """
        with open('../datas/testdatas.yaml', 'r', encoding='utf-8') as f:
            testdata = yaml.safe_load(f)[testflag]
        return testdata
