import os
# 第三个包，需要安装，pip install requests
import requests
# 用xpath分析当前页面的数据，获取数据，需要安装 pip install lxml
from lxml import etree

from urllib import request

from threading import Thread

from queue import Queue

url_queue = Queue()
img_queue = Queue()


base_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(base_dir, 'images')

def parse_url():

    while True:

        if url_queue.empty():
            break

        url, i = url_queue.get()

        # 请求url
        res = requests.get(url)

        # 获取页面的数据
        con = res.text

        # 创建 以页面为名字的目录
        # 1，先判断文件夹是否存在
        page_path = os.path.join(img_path, i)
        if not os.path.exists(page_path):
            os.mkdir(page_path)


        html = etree.HTML(con)

        srcs = html.xpath("//ul[@class='list-group']//img/@data-original")
        alts = html.xpath("//ul[@class='list-group']//img/@alt")

        for src, alt in zip(srcs, alts):
            ext = os.path.splitext(src)[1]
            img_name = alt + ext
            img_paths = os.path.join(page_path, img_name)
            # urlretrieve 用来下载图片
            img_queue.put((src, img_paths))



def download():

    while True:

        if url_queue.empty() and img_queue.empty():
            break

        src, img_paths = img_queue.get()
        request.urlretrieve(src, img_paths)





if __name__ == '__main__':

    for i in range(1,7):
        url = f'http://www.doutula.com/photo/list/?page={i}'
        url_queue.put((url, str(i)))


    data = []
    for i in range(0,3):
        t = Thread(target=parse_url)
        data.append(t)


    for i in range(0,3):
        t = Thread(target=download)
        data.append(t)


    for i in data:
        i.start()
