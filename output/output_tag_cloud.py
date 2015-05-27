# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist output_tag_cloud.py

import re
import urllib2

book_url = 'https://api.douban.com/v2/book/1139336'
response = urllib2.urlopen(book_url)
s = re.findall('"tags".*?]', response.read()) 
#lazy get from json book information

print s # test 
