import requests

res = requests.get("https://www.baidu.com/")
html = res.text
print('hello world')

print(res)
print(html)
print(type(html))

