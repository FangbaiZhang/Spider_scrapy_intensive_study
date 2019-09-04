# -*- coding:utf-8 -*-

import requests
from urllib import parse

class TiebaSpider():

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "http://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%86%8A%E7%8C%AB"}

    # 构建要访问的URL地址列表
    def get_url_list(self):
        url_list = list()
        for i in range(1000):
            url_list.append(self.url_temp.format(i*50))
        return url_list

    # 获取页面内容
    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        html = response.content.decode()
        return html

    # 保存获取的页面内容
    def save_html(self, html_str, page_num):
        os_path = "./001_tieba_spider"
        file_path = os_path + "/{}吧第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    # 主程序逻辑实现
    def run(self):
        # 1. 构造url列表
        url_list = self.get_url_list()
        # 2. 遍历，发送请求，获取，存储
        for url in url_list:
            html_str = self.parse_url(url)
            # 3. 保存
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == "__main__":
    name = input("贴吧名字:")
    tieba_spider = TiebaSpider(name)
    tieba_spider.run()