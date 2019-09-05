# -*- coding:utf-8 -*-

import requests

url = "https://www.baidu.com"
# 传入的请求头信息都需要使用字典格式
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

# 使用get请求，传入网址，请求头
response = requests.get(url=url, headers=headers)

print(response.status_code)

# 解码类型：根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
# 可以指定编码
# 类型：str
response.encoding = "utf-8"
print(type(response.text))

# - 类型：bytes
# - 解码类型： 没有指定,默认utf-8
# - 如何修改编码方式：response.content.decode(“utf-8”)
print(type(response.content))
print(type(response.content.decode()))