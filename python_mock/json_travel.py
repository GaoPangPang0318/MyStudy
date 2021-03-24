# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File         : json_travel
# @Time         : 2021/3/23 22:21
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import json
from mitmproxy import http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" \
                in flow.request.pretty_url:
        # 打开文件，读取文件数据，作为响应，给返回
            data = json.loads(flow.response.text)
            flow.response.text = json.dumps(self.modify_json(data))

    def modify_json(self,data):
        if isinstance(data,dict):
            for k,v in data.items():
                if k=="items":



addons = [
    Counter()
]

# if __name__ == '__main__':
    # """
    # json.loads 和json.load的区别：
    #     json.loads()参数是字符串。
    #     json.load()参数是文件对象。
    # """
    # data=json.load(open("quote_xueqiustock.json",encoding='utf-8'))
    # new_data=Counter().json_travel(data)
    # with open("new.json","w",encoding="utf-8") as f:
    #     json.dump(new_data,fp=f,indent=2)



