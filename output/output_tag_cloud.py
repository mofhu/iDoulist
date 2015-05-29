# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist output_tag_cloud.py

import re
import urllib2

frequencies = []

def get_frequencies_book(book_url, frequencies):
    response = urllib2.urlopen(book_url)
    raw_data = re.findall('"tags".*?]', response.read())
    tag_list = []
    for i in raw_data: # 注意这里一定要写成这样的形式: 如果写成 str(raw_data) 会转换字符格式
        # print i
        raw_list = re.findall('{"count".*?}', i) # extract tags from the big list, 已经是列表了
    for j in raw_list: # raw_list 保存所有的豆列信息组, count:名字格式
        duplicate = 0
        i_count = re.search('\d+', j) # get counts

        i_tag = re.search(',.*?,', j)
        i_tag0 = re.sub(',"name":"', '', i_tag.group()) # cut front string
        i_tag = re.sub('",', '', i_tag0) # cut later string
        #print i_tag
        #print [unicode(i_tag, 'utf8'), i_count.group()] # unicode 编码才可正确打印
        for known_tag in frequencies:
            if known_tag[0] == unicode(i_tag, 'utf8'):
                known_tag[1] += int(i_count.group())
                print known_tag[0], known_tag[1], 'get'#testing
                duplicate = 1
        if not duplicate:
            frequencies.append([unicode(i_tag, 'utf8'), float(i_count.group())])

def get_frequencies_list(book_list):
    global frequencies
    frequencies = []
    for i in book_list:
        # get book num
        i_book_num = re.search('\d+', i)
        # print i_book_num.group()
        book_url = 'https://api.douban.com/v2/book/' + i_book_num.group() + '?apikey=001ea9652efc79eb005bfc2f8cf56dc1'
        print book_url
        # get frequencies of this book
        get_frequencies_book(book_url, frequencies)

# print frequencies

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def tag_cloud(book_list):
    path.exists('/Users/FrankHu/Library/Fonts/WeibeiSC-Bold.otf')

## frequencies = [[u'C', 2144], [u'编程', 1399], [u'c语言', 1363], [u'计算机', 803], [u'程序设计', 715]]
    get_frequencies_list(book_list)
    for i in frequencies:
        print i[0], i[1]
    wordcloud = WordCloud(font_path='WeibeiSC-Bold.otf').generate_from_frequencies(frequencies)
# Open a plot of the generated image.
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

#tag_cloud(book_list)