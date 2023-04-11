#!/usr/bin/env python
"""
生成带有图片形状的词云
"""

import os
from os import path
from PIL import Image
import numpy as np
import random
import jieba
from wordcloud import WordCloud, ImageColorGenerator

# 获取数据路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# 设置停用词路径
stopwords_path = d + '/wc_cn/stopwords_cn_en.txt'

# 设置字体路径
font_path = d + '/fonts/smiley-sans/SmileySans-Oblique.otf'

# 读取文本文件
text = open(path.join(d, d + '/blackboard.md'), encoding='utf-8').read()

# 图片路径
image_path = '/wc_cn/LuXun_color.jpg'

# 读取图片
mask = np.array(Image.open(d+image_path))

# 定义随机颜色函数
colors = ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800', '#FF5722']
color_func = lambda *args, **kwargs: colors[random.randint(0, len(colors)-1)]

# 词云配置
wc = WordCloud(font_path=font_path,
               background_color='white',
               max_words=2000,
               min_word_length=2,
               max_font_size=150,
               random_state=42,
               width=1280,
               height=728,
               margin=3,
               mask=mask)

# 分词处理
def jieba_processing_txt(text):
    jieba.load_userdict('./wc_cn/userdict.txt')
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)

    with open(stopwords_path, encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.splitlines()

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)

# 生成词云
wordcloud = wc.generate(jieba_processing_txt(text))

# 根据图片形状着色
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func=color_func)

# 显示词云
import matplotlib.pyplot as plt
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存词云图片
wc.to_file('wordcloud.png')
