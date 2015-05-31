# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist output_tag_cloud.py

import re
import urllib2
import os
from os import path
from wordcloud import WordCloud

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
                known_tag[1] += float(i_count.group())
                print known_tag[0], known_tag[1], 'get'#testing
                duplicate = 1
        if not duplicate:
            frequencies.append([unicode(i_tag, 'utf8'), float(i_count.group())])
    return frequencies

def get_frequencies_list(book_list, frequencies):
    frequencies = []
    for i in book_list:
        # get book num
        i_book_num = re.search('\d+', i)
        # print i_book_num.group()
        book_url = 'https://api.douban.com/v2/book/' + i_book_num.group() + '?apikey=001ea9652efc79eb005bfc2f8cf56dc1'
        print book_url
        # get frequencies of this book
        get_frequencies_book(book_url, frequencies)
    return frequencies

def bubble_sort(fre_list):
    bubble_sorted = [] # sorted sequence
    i = 0
    # bubble bubble_sorted
    while i < len(fre_list):
        j = 0
        while j < i:
            if bubble_sorted[j][1] < fre_list[i][1]:
                break
            j += 1
        bubble_sorted.insert(j, fre_list[i])
        i += 1
    fre_list = bubble_sorted
    return fre_list

def tag_cloud(book_list):
    frequencies = []
    path.exists('/Users/FrankHu/Library/Fonts/WeibeiSC-Bold.otf')

    frequencies = get_frequencies_list(book_list, frequencies)
    
    # use one/two functions to sort and normalize data, for better visualization
    # 也可修改 word cloud, 但用户修改起来不现实, 所以暂时把数据处理成适合 word cloud 进行可视化的形式.
    frequencies = bubble_sort(frequencies)

    wordcloud = WordCloud(font_path='WeibeiSC-Bold.otf', width=800, height=400, max_words=100, max_font_size=250).generate_from_frequencies(frequencies).to_file('iDoulist_tag_cloud.png')
    os.system('open iDoulist_tag_cloud.png') # output tag cloud picture

# test code
def main():

    frequencies = [[u'Linux', 2795.0], [u'\u601d\u7ef4', 1418.0], [u'\u8ba1\u7b97\u673a', 1191.0], 
                   [u'\u7f16\u7a0b', 1003.0], [u'\u8f6f\u4ef6\u5f00\u53d1', 704.0], [u'\u7a0b\u5e8f\u5458', 649.0], 
                   [u'\u64cd\u4f5c\u7cfb\u7edf', 632.0], [u'\u8f6f\u4ef6\u5de5\u7a0b', 555.0], 
                   [u'\u7a0b\u5e8f\u5458\u7684\u601d\u7ef4\u4fee\u70bc', 470.0], [u'\u9e1f\u54e5', 450.0], 
                   [u'Linux\\/Unix', 283.0], [u'\u8ba4\u77e5', 252.0], [u'\u7f16\u7a0b\u827a\u672f', 190.0], 
                   [u'IT', 185.0], [u'\u7a0b\u5e8f\u8bbe\u8ba1', 173.0], [u'\u7a0b\u5e8f\u5458\u7684\u4fee\u70bc\u4e4b\u9053', 152.0], 
                   [u'linux', 143.0], [u'vim', 125.0], [u'\u6280\u672f', 121.0], [u'\u9879\u76ee\u7ba1\u7406', 67.0], 
                   [u'\u8ba1\u7b97\u673a\u79d1\u5b66', 45.0], [u'\u5de5\u5177', 41.0], [u'\u6559\u80b2', 37.0], 
                   [u'programming', 36.0], [u'Python', 33.0], [u'Vim', 28.0], [u'vi', 22.0], [u'\u5165\u95e8', 8.0], 
                   [u'python\u521d\u5b66', 6.0], [u'\u7f16\u7a0b\u8bed\u8a00', 3.0], [u'\u7a0b\u5e8f', 2.0]]

    wordcloud = WordCloud(font_path='WeibeiSC-Bold.otf', width=800, height=400, max_words=100, max_font_size=300).generate_from_frequencies(frequencies).to_file('iDoulist_tag_cloud.png')
    os.system('open iDoulist_tag_cloud.png')

if __name__=='__main__':
    main()