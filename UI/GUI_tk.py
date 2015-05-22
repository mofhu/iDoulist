# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - UI module

from Tkinter import *
import ttk
from . import function0_UI

input_url = function0_UI.doulist_input()

def input_test(*args):
    try:
    	value = str(doulist_input1.get())
        print 'test %s' % doulist_input1.get()
        status.set(value)
    except ValueError:
    	pass

def output_test(*args):
    try:
        print 'test %s' % doulist_input2.get()
    except ValueError:
    	pass

root = Tk()
root.title("iDoulist")

mainframe = ttk.Frame(root, padding="3 3 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Input Doulist url1").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Input Doulist url2").grid(column=2, row=1, sticky=W)
status = StringVar()
status.set('List is blank')
ttk.Label(mainframe, textvariable=status).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Input", command=input_test).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Output", command=output_test).grid(column=3, row=3, sticky=W)

url1 = StringVar()
doulist_input1 = ttk.Entry(mainframe, width=25, textvariable=url1)
doulist_input1.grid(column=1, row=2, sticky=W)
#print 'current value1 is %s' % doulist_input1.get()
url2 = StringVar()
doulist_input2 = ttk.Entry(mainframe, width=25, textvariable=url2)
doulist_input2.grid(column=2, row=2, sticky=W)
#print 'current value2 is %s' % doulist_input2.get()

root.mainloop()
