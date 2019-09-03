# -*- coding:utf-8 -*-

# 百度搜索，网址wd=熊猫就是params参数
# 请求头里面的熊猫使用了url编码%xx%xx
# https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%86%8A%E7%8C%AB

import requests
from urllib import parse

url = "https://www.baidu.com/baidu?"
# 传入的请求头信息都需要使用字典格式
headers = {"User-Agent": "https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%86%8A%E7%8C%AB"}
# 参数根据网址规则传入，字典格式
params = {"wd": "熊猫"}

# 使用get请求，传入网址，请求头，参数
response = requests.get(url=url, headers=headers, params=params)

# 查看响应网址
print(response.url)
# url地址编码解码
print(parse.unquote(response.url))

# 查看状态码
print(response.status_code)

# 查看响应的页面内容，已经格式化处理，已经自动空格对齐，已自动解码为字符串格式
print(response.text)
print(type(response.text))
print('*' * 100)

# 查看响应页面内容，未进行格式化处理，还是原始字节格式
print(response.content)
print(type(response.content))

# 如果使用urllib库中的request.urlopen直接得到的还是字节格式，需要手动decode解码为字符串格式
# 参考Spider_development_study_note项目中的001文件夹案例