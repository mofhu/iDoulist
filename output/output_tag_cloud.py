# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist output_tag_cloud.py

import re
import urllib2

book_url = 'https://api.douban.com/v2/book/1139336'

def response(book_url):
    response = urllib2.urlopen(book_url)
    raw_data = re.findall('"tags".*?]', response.read())
    tag_list = []
    for i in raw_data: # 注意这里一定要写成这样的形式: 如果写成 str(raw_data) 会转换字符格式
        print i
        raw_list = re.findall('{"count".*?}', i) # extract tags from the big list, 已经是列表了
    for j in raw_list:
        i_count = re.search('\d+', j) # get counts
        print i_count.group()
        i_tag = re.search(',.*?,', j)
        # print i_tag.group()
        i_tag0 = re.sub(',"name":"', '', i_tag.group()) # cut front string
        i_tag = re.sub('",', '', i_tag0) # cut later string
        print i_tag

response(book_url)