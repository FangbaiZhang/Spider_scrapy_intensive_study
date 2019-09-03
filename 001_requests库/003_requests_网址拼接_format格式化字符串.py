# -*- coding:utf-8 -*-
# 002案例可以直接使用字符串拼接更加简单

import requests
from urllib import parse

# 字符串拼接，requests.get会自动进行url编码
url = "https://www.baidu.com/baidu?wd={}".format("熊猫")

# 传入的请求头信息都需要使用字典格式
headers = {"User-Agent": "https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%86%8A%E7%8C%AB"}

# 使用get请求，传入网址，请求头
response = requests.get(url=url, headers=headers)

# 查看响应网址
print(response.url)
# url地址编码解码
print(parse.unquote(response.url))