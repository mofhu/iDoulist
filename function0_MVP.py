# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - loader

#import function0_UI
import function0_input
import function0_process
#import function0_output

# get input from CLI

input_url = 'http://www.douban.com/doulist/38390646/'

# input 
doulist_content = function0_input.doulist_url_to_list(input_url)

# process
print function0_process.copy(doulist_content)


# output to file and CLI


