# requests库，适合人类使用的库 HTTP for Humans
# urllib中使用，request.urlopen,繁琐，不适合人类使用，
# urllib不推荐使用，但是可以通过它可以理解网页请求到返回页面内容整个过程原理

# requests 的底层实现其实就是 urllib

# Requests 继承了urllib的所有特性。Requests支持HTTP连接保持和连接池，
# 支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。

# 1. 编码解码问题
# requests请求网页时候会自动url编码，返回页面内容会自动将字节格式解码为字符串格式
# request.urlopen请求网页时候，带参数或者中文需要先手动URL编码，
# 返回页面内容需要先read读取，然后手动decode解码字节为字符串

# urllib库请求返回一个页面步骤
#     url = 'https://guangdiu.com/detail.php?id=6637916'
#     # 打开一个URL然后返回页面的内容
#     rsp = request.urlopen(url)
#     # 把返回的结果读取出来，直接读取的是字节，默认是Unicode
#     html = rsp.read()
#     print(type(html))
#     # 返回的字节，需要解码，解码以后是字符串,默认是UTF-8
#     content = html.decode()
#     # print(content)
#     print(type(content))

# requests库请求返回一个页面步骤：
#     # 字符串拼接，requests.get会自动进行url编码
#     url = "https://www.baidu.com/baidu?wd={}".format("熊猫")
#     # 传入的请求头信息都需要使用字典格式
#     headers = {"User-Agent": "https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%86%8A%E7%8C%AB"}
#     # 使用get请求，传入网址，请求头
#     response = requests.get(url=url, headers=headers)
#     print(response.text) 打印出来就是字符串格式的页面