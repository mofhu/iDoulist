# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - input

import urllib2

response = urllib2.urlopen("http://www.douban.com/doulist/38390646/")
print response.read()