# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist

from UI import function0_UI
#from UI import GUI_tk
from input import function0_input
from process import function0_process, function1_process
from output import function0_output_plain, function2_output

# get input from CLI
#input_url = function0_UI.doulist_input()

# input 
# with input url, std. input is a list, getting its content
#doulist_content = function0_input.doulist_url_to_list(input_url)

# process
# output is a list
#output_list = function0_process.copy(doulist_content)

# output to file and CLI
# output to markdown file and CLI
#function0_output_plain.output_CLI(output_list)
#function0_output_plain.output_file(output_list)

from Tkinter import *
import ttk

idoulist_content = [] # 项目保存的列表: 一切操作围绕着这个列表进行.

def input_test(*args):
    global idoulist_content
    value = str(doulist_input1.get())
    idoulist_content = function0_input.doulist_url_to_list(value)
    print 'test %s' % doulist_input1.get() #test
    length = 'iDoulist: there are %d books in the list now.' % len(idoulist_content)
    status.set(length)

def output_CLI(*args):
    global idoulist_content
    function0_output_plain.output_CLI(idoulist_content)

def output_file(*args):
    global idoulist_content
    function0_output_plain.output_file(idoulist_content)

def output_doulist(*args):
    global idoulist_content
    function2_output.output_doulist(idoulist_content)

def combine(*args):
    global idoulist_content
    list1 = function0_input.doulist_url_to_list(str(doulist_input1.get()))
    list2 = function0_input.doulist_url_to_list(str(doulist_input2.get()))
    idoulist_content = function1_process.combine(list1, list2)
    length = 'iDoulist: there are %d books in the list now.' % len(idoulist_content)
    status.set(length)

root = Tk()
root.title("iDoulist")

mainframe = ttk.Frame(root, padding="3 5 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Input Doulist url1").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Input Doulist url2").grid(column=2, row=1, sticky=W)
status = StringVar()
status.set('iDoulist status: List is blank')
ttk.Label(mainframe, textvariable=status).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text="Input", command=input_test).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Combine Doulists", command=combine).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Books in common", command=combine).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Output CLI", command=output_CLI).grid(column=1, row=5, sticky=W)
ttk.Button(mainframe, text="Output file", command=output_file).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="Output Doulist", command=output_doulist).grid(column=3, row=5, sticky=W)

url1 = StringVar()
doulist_input1 = ttk.Entry(mainframe, width=25, textvariable=url1)
doulist_input1.grid(column=1, row=2, sticky=W)
#print 'current value1 is %s' % doulist_input1.get()
url2 = StringVar()
doulist_input2 = ttk.Entry(mainframe, width=25, textvariable=url2)
doulist_input2.grid(column=2, row=2, sticky=W)
#print 'current value2 is %s' % doulist_input2.get()

root.mainloop()
