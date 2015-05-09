# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - UI module
import re

def doulist_input():
	input_url = raw_input('Please input a Doulist url. e.g. http://www.douban.com/doulist/38390646/ \n')
	# minor bugs in this regular expression
	# e.g. input a doulist link plus xxx
	# http://www.douban.com/doulist/38390646/1234 may lead to fetal error
	if re.match('http://www.douban.com/doulist/[0-9]*/', input_url, ):
		return input_url
	else:
		print 'Wrong input! Please input a valid Doulist url.'
		quit()