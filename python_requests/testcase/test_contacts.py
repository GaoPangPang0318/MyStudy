# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File Name    : test_contacts
# @Time         : 2021/3/28 16:45
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
from typing import Dict, List
import pytest
from python_requests.pages.contacts import Contacts
from python_requests.testcase.testcasebase import TestCaseBase


class TestContacts(TestCaseBase):
    def setup(self):
        self.contacts = Contacts()

    @pytest.mark.parametrize("corpid, corpsecret, result", TestCaseBase.get_testdata('token'))
    def test_token(self, corpid, corpsecret, result: int):
        """
        获取token的测试用例
        :param corpid:
        :param corpsecret:
        :param result: 预期返回的errcode
        """
        r = self.contacts.get_token(corpid, corpsecret)
        assert result == r['errcode']

    @pytest.mark.parametrize("userid,name,mobile,department,otherinfo", TestCaseBase.get_testdata('createmember'))
    def test_createmember(self, userid, name, mobile, department: List, otherinfo: Dict):
        """
        创建用户测试用例
        :param userid: 创建用户需要信息userid
        :param name: 创建用户需要信息name
        :param mobile: 创建用户需要信息mobile
        :param department: 创建用户需要信息department
        :param otherinfo: 创建用户其他信息
        """
        # 是否存在userid
        find_result = self.contacts.get_member(userid)
        # 存在则删除
        if find_result['errmsg'] == 'ok':
            print(f"UserID={userid} is exited.")
            delete_result = self.contacts.delete_member(userid)
            if delete_result['errmsg'] == 'deleted':
                print(f"Successful Delete {userid}.")
        # 创建成员
        r = self.contacts.create_member(userid=userid, name=name, mobile=mobile, department=department, **otherinfo)
        assert r['errmsg'] == 'created'

    @pytest.mark.parametrize("userid,result", TestCaseBase.get_testdata('getmember'))
    def test_getmember(self, userid, result: int):
        """
        获取用户信息测试用例
        :param userid:
        :param result: 预期返回错误码
        """
        r = self.contacts.get_member(userid=userid)
        assert r['errcode'] == result

    @pytest.mark.parametrize("userid,changeinfo", TestCaseBase.get_testdata('updatemember'))
    def test_updatemember(self, userid, changeinfo: Dict):
        """
        修改已有用户信息测试用例
        :param userid:
        :param changeinfo: 要修改的参数
        """
        r = self.contacts.update_member(userid=userid, **changeinfo)
        assert r['errcode'] == 0

    @pytest.mark.parametrize("userid,result", TestCaseBase.get_testdata('deletemember'))
    def test_deletemember(self, userid, result: int):
        """
        删除用户的测试用例
        :param userid:
        :param result: 预期返回的errcode
        """
        r = self.contacts.delete_member(userid=userid)
        assert r['errcode'] == result
#
