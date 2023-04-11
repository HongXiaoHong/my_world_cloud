#!/usr/bin/env python
"""
自定义形状和中文词云的例子
==========================

这个例子展示了如何从文本和自定义形状生成一个中文词云，使用Jieba进行中文分词和处理。

这个例子的自定义形状是一个中国地图的矢量图形。
"""

import os
import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# 获取数据路径
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# 读取文本数据
text = open(os.path.join(d, "blackboard.md"), encoding="utf-8").read()

# 加载自定义词典
jieba.load_userdict(os.path.join(d, "userdict.txt"))

# 读取中国地图矢量图形
mask = np.array(Image.open(os.path.join(d, "parrot-by-jose-mari-gimenez2.jpg")))

# 创建WordCloud对象
wc = WordCloud(
    font_path=os.path.join(d, "SmileySans-Oblique.otf"),
    background_color="white",
    max_words=2000,
    mask=mask,
    max_font_size=100,
    random_state=42,
)

# 对文本进行分词和处理
word_list = jieba.lcut(text)
processed_text = " ".join(word_list)

# 生成词云
wc.generate(processed_text)

# 从图片中提取颜色
image_colors = ImageColorGenerator(mask)

# 将图片颜色应用到词云中
wc.recolor(color_func=image_colors)

# 展示词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
