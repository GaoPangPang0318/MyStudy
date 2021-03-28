# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File Name    : wecombase.py
# @Time         : 2021/3/27 16:32
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import requests
import yaml
from requests import Session


class WeComBase:
    def __init__(self):
        # 实例化Session类对象
        self.session = Session()
        # 从yaml文件中获取corpid和corpsecret
        with open('../datas/contactsdatas.yaml', 'r', encoding='utf-8') as f:
            corpinfo = yaml.safe_load(f)
        # 获取token参数1：企业ID
        self.corpid = corpinfo['corpid']
        # 获取token参数2：应用的凭证密钥
        self.corpsecret = corpinfo['corpsecret']
        # 将获取的token保存在session中
        self.session.params["access_token"] = self.get_token().get('access_token')

    def get_token(self, corpid=None, corpsecret=None):
        """
        获取token的函数
        :param corpid:企业ID
        :param corpsecret: 应用的凭证密钥
        :return: 获取access_token接口响应内容的json格式数据
        """
        if corpid == 'None' or corpid is None:
            corpid = self.corpid
        if corpsecret == 'None' or corpsecret is None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        return r.json()
