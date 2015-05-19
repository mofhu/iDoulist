# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 1 - MVP loader

#import function0_UI
from UI import function0_UI
from input import function0_input
from process import function1_process
from output import function1_output_plain

# get input from CLI
input_url1 = function0_UI.doulist_input()
input_url2 = function0_UI.doulist_input()

# input 
# with input url, std. input is a list, getting its content
doulist_content1 = function0_input.doulist_url_to_list(input_url1)
doulist_content2 = function0_input.doulist_url_to_list(input_url2)

# process
# combine;common;1-2;2-1
combine = function1_process.combine(doulist_content1, doulist_content2)
common = function1_process.common(doulist_content1, doulist_content2)
content1_2 = function1_process.minus(doulist_content1, doulist_content2)
content2_1 = function1_process.minus(doulist_content2, doulist_content1)

# output
# output to markdown file and CLI
function1_output_plain.output_CLI('Combined list', combine)
function1_output_plain.output_CLI('Common list', common)
function1_output_plain.output_CLI('Doulist1 - Doulist 2', content1_2)
function1_output_plain.output_CLI('Doulist2 - Doulist 1', content2_1)

function1_output_plain.output_file('Common list:', common)