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
        try:
            r = self.contacts.create_member(userid=userid, name=name, mobile=mobile, department=department, **otherinfo)
        finally:
            delete_result = self.contacts.delete_member(userid)
        assert r['errmsg'] == 'created'
        assert delete_result['errcode']==0

    @pytest.mark.parametrize("userid,result", TestCaseBase.get_testdata('getmember'))
    def test_getmember(self, userid, result: int):
        """
        获取用户信息测试用例
        :param userid:
        :param result: 预期返回错误码
        """
        self.contacts.create_member('lisi','李四','18320202022',[1,2])
        try:
            r = self.contacts.get_member(userid=userid)
        finally:
            self.contacts.delete_member(userid)
        assert r['errcode'] == result


    @pytest.mark.parametrize("userid,changeinfo", TestCaseBase.get_testdata('updatemember'))
    def test_updatemember(self, userid, changeinfo: Dict):
        """
        修改已有用户信息测试用例
        :param userid:
        :param changeinfo: 要修改的参数
        """
        self.contacts.create_member('zhangsan','王二','18320202023',[1,3],gender=2,position='研发经理')
        try:
            r = self.contacts.update_member(userid=userid, **changeinfo)
        finally:
            self.contacts.delete_member(userid)
        assert r['errcode'] == 0

    @pytest.mark.parametrize("userid,result", TestCaseBase.get_testdata('deletemember'))
    def test_deletemember(self, userid, result: int):
        """
        删除用户的测试用例
        :param userid:
        :param result: 预期返回的errcode
        """
        self.contacts.create_member('lisi', '李四', '18320202022', [1, 2])
        r = self.contacts.delete_member(userid=userid)
        assert r['errcode'] == result

