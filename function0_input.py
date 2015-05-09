# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - input

import re
import urllib2

# get url from UI module for test
def main():
    input_url = 'http://www.douban.com/doulist/38390646/'
    doulist_content = doulist_url_to_list(input_url)
    print doulist_content

# the list doulist_content is to be sent to process module

def doulist_url_to_list(doulist_url):
	# use urllib to get html data from url
    response = urllib2.urlopen(doulist_url)
	# use re.findall to get a raw match (as douban.com show twice a input list.)
	# as the time to remove duplicate accumulates, better way is match only once,
	# and then cut unwanted parts (of course its an better algorithm as it is O(n))
    doulist_content = re.findall('http://book.douban.com/subject/[0-9]*/', 
	                              response.read())
    # limited function now: only first 25 book in a long list is get.
    remove_duplicate_element(doulist_content)
    return doulist_content

# remove duplicate of a list
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