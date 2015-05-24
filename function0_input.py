# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - input

import re
import urllib2

# get url from UI module for test
def main():
    input_url = 'https://github.com/Frank-the-Obscure/iDoulist/blob/master/testfile/stdio-function0.md'
    doulist_content = doulist_url_to_list(input_url)
    print doulist_content

# the list doulist_content is to be sent to process module

def doulist_url_to_list(doulist_url):
    # use urllib to get html data from url
    i = 0
    doulist_content = []
    while 1:
        response = urllib2.urlopen(doulist_url)
        # use re.findall to get a raw match (as douban.com show twice a input list.)
        # as the time to remove duplicate accumulates, better way is match only once,
        # and then cut unwanted parts (of course its an better algorithm as it is O(n))
        s = re.findall('http://book.douban.com/subject/[0-9]*/', 
                                   response.read())
        if not s:
            break
        else:
            remove_duplicate_element(s)
            for j in s:
                doulist_content.append(j)
            i += 25
    # limited function now: only first 25 book in a long list is get.

    #remove_duplicate_element(doulist_content)
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