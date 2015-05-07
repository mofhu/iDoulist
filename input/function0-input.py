# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - input

import re
import urllib2

input_url = 'http://www.douban.com/doulist/38390646/'
response = urllib2.urlopen(input_url)

doulist_content = re.findall('http://book.douban.com/subject/[0-9]*/', response.read())

print doulist_content

'''
 doulist_content = 
['http://book.douban.com/subject/1139336/', 
 'http://book.douban.com/subject/1139336/', 
 'http://book.douban.com/subject/25724948/', 
 'http://book.douban.com/subject/25724948/']
'''

# remove duplicate

i = 0
while i <= len(doulist_content) - 1:
    j = i + 1
    while j <= len(doulist_content) - 1:
        if doulist_content[i] == doulist_content[j]:
            del doulist_content[j]
        j += 1
    i += 1

print doulist_content
