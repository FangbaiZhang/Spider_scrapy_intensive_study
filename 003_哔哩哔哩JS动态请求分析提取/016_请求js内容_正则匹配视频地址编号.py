# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: 18200116656@qq.com
Blog: https://blog.csdn.net/u011318077
Date:  21:03
Desc:
'''

import json
import re
import requests

def json_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
    }
    response = requests.get(url, headers=headers, timeout=3)
    js_info = response.content.decode() # 返回内容还是一个json格式的字符串
    # print(type(js_info))
    # html = json.loads(js_info) # 转换为python支持的字典格式
    # print(type(html))
    # print(html)
    # json格式字符中查找内容,查找aid对应的值即视频的编号
    ret = re.findall(r'''"aid":(\d+),''', js_info)
    print(ret)



if __name__ == '__main__':
    url = "https://api.bilibili.com/x/web-interface/newlist?&rid=22&type=0&pn=3&ps=20"
    json_request(url)