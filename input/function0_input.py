# -*- coding: utf-8 -*-
# Author Frank Hu , nicetag
# iDoulist Function 0 - input

import re
import urllib2
import time

# get url from UI module for test
def main():
    input_url = 'http://www.douban.com/doulist/36764655/'
    doulist_content = doulist_url_to_list(input_url)
    print doulist_content

# the list doulist_content is to be sent to process module

def doulist_url_to_list(doulist_url):
    # use urllib to get html data from url
    if not valid_url(doulist_url):
        print 'iDoulist: 输入的链接格式不正确, 请重新输入!'
        return None
    i = 0
    doulist_content = []
    while 1:
        # print doulist_url + "?start={0}&sort=time".format(i) #final test
        time.sleep(1) # 延迟设置, 防止过于频繁的访问
        response = urllib2.urlopen(doulist_url + "?start={0}&sort=time".format(i))
        # use re.findall to get a raw match (as douban.com show twice a input list.)
        # as the time to remove duplicate accumulates, better way is match only once,
        # and then cut unwanted parts (of course its an better algorithm as it is O(n))
        s = re.findall('http://book.douban.com/subject/[0-9]*/', 
                                   response.read())
        if not s:
            break
        else:
            remove_duplicate_element(s)
            # doulist url
            if 'people' not in doulist_url: 
               for j in s:
                   doulist_content.append(j)
               i += 25 
             # wish/do/collect url   
            else:   
               for j in s:
                   doulist_content.append(j)
               i += 15      

    remove_duplicate_element(doulist_content)
    return doulist_content

# 判断链接是否合法, 使用 re
def valid_url(doulist_url):
    valid = 0
    s = re.search('http://www.douban.com/doulist/[0-9]*/', doulist_url)
    if s: #是豆列链接格式
        valid = 1
        return valid
    else:
        valid = 0
    s = re.search('http://book.douban.com/people/.*?/do|http://book.douban.com/people/.*?/wish|http://book.douban.com/people/.*?/collect', doulist_url)
    # 上述正则表达式使用了吝啬匹配 .*? 以及 或 | 语法
    if s: #是想读链接格式
        valid = 1
        return valid
    else:
        valid = 0
    return valid

# remove duplicate of a list, 这个函数的用途是去重. 
# (用 urllib2 抓取的豆瓣网页中, 书籍链接会出现两次, 因此需去重)
def remove_duplicate_element(list):
    i = 0
    while i <= len(list) - 1:
        j = i + 1
        while j <= len(list) - 1:
            if list[i] == list[j]:
                del list[j]
            j += 1
        i += 1

if __name__=='__main__':
    main()