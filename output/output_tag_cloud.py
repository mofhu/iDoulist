# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist output_tag_cloud.py

import re
import urllib2

book_url = 'https://api.douban.com/v2/book/1139336'

frequencies = []

def get_frequencies(book_url, frequencies):
    response = urllib2.urlopen(book_url)
    raw_data = re.findall('"tags".*?]', response.read())
    tag_list = []
    for i in raw_data: # 注意这里一定要写成这样的形式: 如果写成 str(raw_data) 会转换字符格式
        print i
        raw_list = re.findall('{"count".*?}', i) # extract tags from the big list, 已经是列表了
    for j in raw_list:
        i_count = re.search('\d+', j) # get counts

        i_tag = re.search(',.*?,', j)
        i_tag0 = re.sub(',"name":"', '', i_tag.group()) # cut front string
        i_tag = re.sub('",', '', i_tag0) # cut later string
        #print i_tag
        #print [unicode(i_tag, 'utf8'), i_count.group()] # unicode 编码才可正确打印

        frequencies.append([unicode(i_tag, 'utf8'), int(i_count.group())])

get_frequencies(book_url, frequencies)

# print frequencies

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

path.exists('/Users/FrankHu/Library/Fonts/WeibeiSC-Bold.otf')

## frequencies = [[u'C', 2144], [u'编程', 1399], [u'c语言', 1363], [u'计算机', 803], [u'程序设计', 715]]

wordcloud = WordCloud(font_path='WeibeiSC-Bold.otf').generate_from_frequencies(frequencies)
# Open a plot of the generated image.
plt.imshow(wordcloud)
plt.axis("off")
plt.show()