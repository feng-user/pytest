import os


# __file__ 找到 当前文件的 路径,可能是绝对路径，也可能是相对路径
# os.path.abspath 获取文件的绝对路径
# os.path.dirname 获取当前文件地址的上一级目录

base_dir = os.path.dirname(os.path.abspath(__file__))

# os.path.join 连接两个路径地址
img_path = os.path.join(base_dir, 'img')

# os.path.exists 判断 文件或者 文件夹 是否存在
if not os.path.exists(img_path):

    # os.mkdir 创建文件夹
    os.mkdir(img_path)
