#!/usr/bin/env python
"""
最简单的例子
===============

使用默认参数从编程语言生成一个方形词云
"""

import os

from os import path
from wordcloud import WordCloud

# 获取数据路径
# 在 IPython notebook 下则使用 getcwd()
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


# 读取 constitution.txt 的文本
text = open(path.join(d, 'code_language.txt')).read()

# 生成一个词云图片
wordcloud = WordCloud().generate(text)

# 使用 matplotlib 展示生成图片
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# 没有 matplotlib 也可以使用 pil 展示图片
# image = wordcloud.to_image()
# image.show()