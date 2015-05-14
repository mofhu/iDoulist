# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - MVP loader

#import function0_UI
from UI import function0_UI
from input import function0_input
from process import function0_process
from output import function0_output
from output import function2_output

# get input from CLI
input_url = function0_UI.doulist_input()

# input 
# with input url, std. input is a list, getting its content
doulist_content = function0_input.doulist_url_to_list(input_url)

# process
# output is a list
output_list = function0_process.copy(doulist_content)

print output_list # debug
# output to file and CLI
# output to markdown file and CLI
function0_output.output_CLI(output_list)
function0_output.output_file(output_list)
function2_output.output_doulist(output_list)