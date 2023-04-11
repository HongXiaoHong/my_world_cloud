#!/usr/bin/env python
"""
最简单的例子
===============

使用默认参数从编程语言生成一个方形词云
"""
import random
import jieba
import os

from os import path
from wordcloud import WordCloud

# 获取数据路径
# 在 IPython notebook 下则使用 getcwd()
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


stopwords_path = d + '/stopwords_cn_en.txt'
# Chinese fonts must be set
font_path = d + '/SmileySans-Oblique.otf'


# define a random color function
colors = ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800', '#FF5722']
color_func = lambda *args, **kwargs: colors[random.randint(0, len(colors)-1)]


# The function for processing text with Jieba
def jieba_processing_txt(text):
    # 加载自定义词典
    jieba.load_userdict('./userdict.txt')

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


# 读取 constitution.txt 的文本
text = open(path.join(d, d + '/blackboard.md'), encoding='utf-8').read()
text = str(text)

wc = WordCloud(font_path=font_path, 
               max_words=25, 
               min_word_length=2,
               max_font_size=150, 
               random_state=42, 
               width=1280, 
               height=728, 
               margin=3,
               background_color='#222222',
               )

# 生成一个词云图片
wordcloud = wc.generate(jieba_processing_txt(text))
wc.recolor(color_func=color_func)

with open('wordcloud.png', 'wb') as f:
    wordcloud.to_image().save(f, 'PNG')
