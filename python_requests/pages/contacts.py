# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File Name    : contacts
# @Time         : 2021/3/27 17:09
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
from typing import List
from python_requests.pages.wecombase import WeComBase


class Contacts(WeComBase):
    def create_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        """
        创建成员
        """
        create_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            'userid': userid,
            'name': name,
            'mobile': mobile,
            'department': department
        }
        data.update(kwargs)
        r = self.session.post(url=create_member_url, json=data)
        return r.json()

    def get_member(self, userid: str):
        """
        读取成员
        """
        get_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            'userid': userid
        }
        r = self.session.get(url=get_member_url, params=params)
        print(r.json()['errcode'])
        return r.json()

    def update_member(self, userid: str, **kwargs):
        """
        更新成员
        :param userid:
        :param kwargs:
        :return:
        """
        update_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            'userid': userid
        }
        data.update(kwargs)
        r = self.session.post(url=update_member_url, json=data)
        return r.json()

    def delete_member(self, userid: str):
        """
        删除成员
        :param userid:
        :return:
        """
        delete_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            'userid': userid
        }
        r = self.session.get(url=delete_member_url, params=params)
        return r.json()

    def batchdelete_members(self, useridlist: List[str]):
        """
        批量删除成员
        :param useridlist:
        :return:
        """
        batchdelete_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete'
        data = {
            'useridlist': useridlist
        }
        r = self.session.post(url=batchdelete_member_url, json=data)
        return r.json()

    def get_members_of_department(self, departmentid: int, fetchchild: int):
        """
        获取部门成员
        :param departmentid:
        :param fetchchild:
        :return:
        """
        get_members_of_department_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist'
        params = {
            'department_id': departmentid,
            'fetch_child': fetchchild
        }
        r = self.session.get(url=get_members_of_department_url, params=params)
        return r.json()

    def get_membersinfo_of_department(self, departmentid: int, fetchchild: int):
        """
        获取部门成员详情
        :param departmentid:
        :param fetchchild:
        :return:
        """
        get_membersinfo_of_department = 'https://qyapi.weixin.qq.com/cgi-bin/user/list'
        params = {
            'department_id': departmentid,
            'fetch_child': fetchchild
        }
        r = self.session.get(url=get_membersinfo_of_department, params=params)
        return r.json()
