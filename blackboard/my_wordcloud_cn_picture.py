"""
自定义形状和中文词云的例子
==========================

这个例子展示了如何从文本和自定义形状生成一个中文词云，使用Jieba进行中文分词和处理。

这个例子的自定义形状是一个鹦鹉的矢量图形。
"""

import jieba
import os
import random
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude

from wordcloud import WordCloud, ImageColorGenerator

# 获取数据目录
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()



def get_random_image(directory):
    # 获取目录中所有文件名
    files = os.listdir(directory)

    # 从文件列表中随机选择一张图片
    image_file = random.choice([f for f in files if f.endswith(".jpg") or f.endswith(".png")])

    # 返回图片名
    return image_file


def jieba_processing_txt(text):
    # 加载自定义词典
    jieba.load_userdict('userdict.txt')

    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)

    with open(os.path.join(d, 'stopwords_cn_en.txt'), encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.splitlines()

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)

# 读取文本数据
text = open(os.path.join(d, 'blackboard.md'), encoding="utf-8").read()
text = str(text)

background_image_dir = os.path.join(d, "background")
image_path = os.path.join(background_image_dir, get_random_image(background_image_dir))
print("image_path" + image_path)
# 读取自定义形状
parrot_color = np.array(Image.open(image_path))
# 对形状进行下采样
parrot_color = parrot_color[::3, ::3]

# 创建掩模，用于指定需要生成词云的区域
parrot_mask = parrot_color.copy()
# 将掩模中所有白色区域都视为“掩蔽区”，不参与词云的生成
parrot_mask[parrot_mask.sum(axis=2) == 0] = 255

# 对掩模进行微调，加强掩蔽区和非掩蔽区之间的边界，避免颜色混在一起
edges = np.mean([gaussian_gradient_magnitude(parrot_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
parrot_mask[edges > .08] = 255

# 创建WordCloud对象
wc = WordCloud(font_path=os.path.join(d, 'SmileySans-Oblique.otf'),
               max_words=2000, 
               mask=parrot_mask, 
               max_font_size=40, 
               random_state=42, 
               relative_scaling=0)

# 对文本进行分词和处理，并生成词云
wc.generate(jieba_processing_txt(text))
# plt.imshow(wc)

# 从图片中提取颜色，并将颜色应用到词云中
image_colors = ImageColorGenerator(parrot_color)
wc.recolor(color_func=image_colors)

# 显示词云
# plt.figure(figsize=(10, 10))
# plt.imshow(wc, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# 输出词云图像到文件
wc.to_file("wordcloud.png")
