import os
# 第三个包，需要安装，pip install requests
import requests
# 用xpath分析当前页面的数据，获取数据，需要安装 pip install lxml
from lxml import etree

from urllib import request

from threading import Thread


base_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(base_dir, 'images')

def parse_url(url, i):
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
        # urlretrieve 用来下载图片
        request.urlretrieve(src, os.path.join(page_path, img_name))




def run1():
    for i in range(1,3):
        url = f'http://www.doutula.com/photo/list/?page={i}'
        parse_url(url, str(i))

def run2():
    for i in range(3,5):
        url = f'http://www.doutula.com/photo/list/?page={i}'
        parse_url(url, str(i))


def run3():
    for i in range(5,7):
        url = f'http://www.doutula.com/photo/list/?page={i}'
        parse_url(url, str(i))



if __name__ == '__main__':

    t1 = Thread(target=run1)
    t2 = Thread(target=run2)
    t3 = Thread(target=run3)

    t1.start()
    t2.start()
    t3.start()



